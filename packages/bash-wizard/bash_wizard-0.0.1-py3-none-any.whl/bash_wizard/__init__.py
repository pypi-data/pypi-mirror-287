import requests
import json
import sys
import subprocess
from bashcolor import colorize, LIGHT_PURPLE, RED, BOLD, UNDERLINE

template = {
    "bash_command": "",
    "command_explanation": ""
}

def show_help_and_exit():
    help_message = f"Welcome to {colorize('🧙 Bash Wizard', LIGHT_PURPLE)} 🪄\nbash_wizard is an AI-powered wizard that creates bash commands to perform the action you need!\n\nUsage: bash_wizard <command_request>\nArguments:\n\t<command_request>: description of what the command should do.\n\nExample:\n\tbash_wizard remove all __pycache__ dir include subdirs\n\tbash_wizard find all .gitkeep files in subdir and add to .gitignore with ! prefix\n"
    print(help_message)
    exit(0)


def call_ollama(description:str) -> dict:
    prompt = f"You are a linux bash command line wizard, please answer how can I do: \n {description}. \nUse the following template: {json.dumps(template)}."
    data = {
        "prompt": prompt,
        "model": "llama3",
        "format": "json",
        "stream": False,
        "options": {"temperature": 2.5, "top_p": 0.99, "top_k": 100},
    }
    try:
        response = requests.post("http://localhost:11434/api/generate", json=data, stream=False)
        response.raise_for_status()
        response_data = json.loads(response.text)['response']
    except requests.RequestException as e:
        print(f"💥 {colorize('OOPS', RED)} 💥\nI couldn't access Ollama, check if the service is up and try again! {colorize('')}")
        exit(1)

    return json.loads(response_data)

  
def main():
    description = ' '.join(sys.argv[1:])
    if not description or description == '-h':
        show_help_and_exit()

    print(f"{colorize('🧙 Bash Wizard', LIGHT_PURPLE)} is solving 🔮 {colorize(description, effects=[UNDERLINE])} 🔮", colorize(""))
    response = call_ollama(description)
    explain = response['command_explanation'].strip()
    commandline = response['bash_command'].strip()

    output = f"{colorize('Bash Wizard', LIGHT_PURPLE, effects=[])} suggests the following command:\n\n🪄 {colorize(commandline, effects=[BOLD])}{colorize('')}\n\n🧙 Explanation:\n{explain}\n\nDo you want to execute 🪄 {colorize(commandline, effects=[BOLD])}{colorize('')} (y/[n])? "
    user_input = input(output).strip().lower()
    if user_input == 'y':
        print(f"\n\n{commandline}")
        subprocess.run(commandline, shell=True)
    else:
        print("🧙 Okay bye!")
  
  
if __name__ == "__main__":
    main()