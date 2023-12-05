# Written: 10/20/23
# Purpose: Simple cyberpunky menu option for future projects.
import os
from typing import Dict, Callable #helps define hinting & type checking for function parameters

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def formatted_header(pagetitle: str) -> None:
    print(f"\033[96m\\\\ \033[93m{pagetitle} \033[96m\\\\\\\\\\\\\\\\\\\\\n")

def formatted_prompt(prompt: str) -> str:
    return input(f"\n\033[93m{prompt}: \033[96m")

def formatted_msg(message: str, isError: bool) -> None:
    if isError:
        print(f"\033[93m>>> \033[91m{message}\033[0m")
    else:
        print(f"\033[93m>>> \033[96m{message}\033[0m")

def formatted_list(listitems: list) -> None:
    #creates a numbered list for menus
    for num, option_name in enumerate(listitems, start=1):
        print(f"\033[38;5;93m[\033[93m{num}\033[38;5;93m] \033[96m{option_name}")

def create_menu(menuname: str, menuoptions: Dict[str, Callable], ismain: bool) -> None:
    """
    Create and display a menu.

    : menuname: string of the title of the menu page
    : menuoptions: dictionary of option name (str) and a callable function (Callable)
    : ismain: determines if it's the main menu or submenu. This displays "exit" for main & "back" elsewhere.
    """

    # Pre-convert the dictionary keys to a list
    options_list = list(menuoptions.keys())

    while True:
        clear_screen()
        formatted_header(menuname)
        formatted_list(options_list)

        exit_back_option = "Exit" if ismain else "Back"
        print(f"\033[38;5;93m[\033[93m{len(options_list) + 1}\033[38;5;93m] \033[96m{exit_back_option}\033[0m")

        try:
            choice = int(formatted_prompt("Enter your choice"))
        except ValueError:
            input("Invalid choice. Try again: ")
            continue

        # If the choice is within the options_list, find the corresponding function and execute it
        if 1 <= choice <= len(options_list):
            chosen_option = options_list[choice - 1]
            chosen_function = menuoptions.get(chosen_option)
            if chosen_function:
                chosen_function()
        elif choice == len(options_list) + 1:
            if ismain:
                print(f"Exiting...\n\033[0m\n")
            return
        else:
            input("Invalid choice. Try again: ")


