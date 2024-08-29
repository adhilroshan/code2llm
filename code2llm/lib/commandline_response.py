
import platform
import os
import pyfiglet
from colorama import Fore


def commandline_response():
    art = pyfiglet.figlet_format("Code2LLM", font="isometric1", width=100)
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
    print(Fore.BLUE + art)
    print('')
    print("--------------------------------------------------------------")
    print('')
    print("Welcome to Code2LLM!")
    print(Fore.RESET)
    print("Your codebase is now prepared for seamless LLM input.")
    print("Access the ready-to-copy code snippets here:")
    print("\033[1;32mhttp://localhost:2277\033[0m")
    print("--------------------------------------------------------------")
    print("✨ Happy Coding! ✨")
