import click
import os
import code2llm.app as app
import pyfiglet 
from code2llm.initialize import init_cmd
from colorama import Fore

@click.group()
@click.version_option()
def cli():
    art = pyfiglet.figlet_format("Code2LLM", font="isometric1", width=100)
    print(Fore.BLUE + art)
    print("--------------------------------------------------------------")
    # print("Welcome to Code2LLM - Code to Language Model")
    print(Fore.RESET)
    pass

@cli.command()
@click.option('--additional-excludes', '-e', 
              multiple=True, 
              help="Additional file patterns or directories to exclude from processing, e.g., '*.tmp' or 'test_dir/'.")
def init(additional_excludes):
    """Initialize the Code2LLM environment.

    Scans the current directory and prepares the environment with optional additional exclusions.
    """
    directory = os.getcwd()
    init_cmd(directory, additional_excludes)


cli.add_command(app.start)



# @cli.command()
# def run():
#     directory = os.getcwd()
#     run_extraction(directory)

# import click
# import app

# @click.group()
# @click.version_option()
# def cli():
#     pass
# cli.add_command(app.run)

