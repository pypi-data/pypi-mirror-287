from setuptools import setup
from setuptools.command.install import install
import subprocess

class PostInstallCommand(install):
    def run(self):
        install.run(self)
        try:
            subprocess.check_call(['ollama', 'pull', 'llama3'])
        except Exception as e:
            print(f"Error on fetch Ollama model, please check that Ollama is installed and running.\nError: {e}")

setup(
    name='bash_wizard',
    version='0.0.1',
    packages=['bash_wizard'],
    cmdclass={
        'install': PostInstallCommand,
    },
)
