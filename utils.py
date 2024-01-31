import os
import locale
from datetime import datetime
from termcolor import colored
####################
import config
from helpers import print_msg
####################


# Configuring location to get local date and time.
locale.setlocale(locale.LC_TIME, "")


# Return the local date in YYYY-MM-DD format (ISO 8601).
def get_date():
    return datetime.now().strftime("%Y-%m-%d")


# Return time in HH:MM:SS format (ISO 8601).
def get_time():
    return datetime.now().strftime("%H:%M:%S")


# Clear the terminal.
def clear_terminal():
    os.system("cls")


# Remove input if user presses keys when script runs.
def clear_input_buffer():
    import msvcrt  # for Windows
    while msvcrt.kbhit():
        msvcrt.getch()


# Display active backup status.
def display_active_backup_status():
    is_active = config.BACKUP_ACTIVE
    if is_active:
        print(colored(f"Backup active:", "white", attrs=["underline"]) + " " + colored(is_active, "green"), end="\n\n")
    else:
        print(colored(f"Backup active :", "white", attrs=["underline"]) + " " + colored(is_active, "red"), end="\n\n")


# Display how to exit the program.
def display_how_to_exit():
    print_msg("INFO", "To exit the program press CTRL + C")


def display_copy_text_to_print_in_terminal():
    print(colored("Copy text to display in terminal", "light_yellow"), end="\n\n\n\n")