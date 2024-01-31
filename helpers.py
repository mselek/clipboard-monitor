import os
import sys
import re
import platform
from termcolor import cprint
####################
import config
####################


# Custom function to display a message in terminal.
def print_msg(msg_type, msg=None, end="\n", exception_obj=None):
    colors = {
        "INFO": "light_blue",
        "WARNING": "yellow",
        "ERROR": "light_red",
        "EXCEPTION": "light_magenta",
        "DEBUG": "light_cyan"
    }

    if msg_type == "INFO":
        symb = "[?] - "
        msg = symb + msg + end
        cprint(msg, colors["INFO"])

    elif msg_type == "WARNING":
        symb = "/!\ - "
        msg = symb + msg + end
        cprint(msg, colors["WARNING"])

    elif msg_type == "ERROR":
        symb = "[!] - "
        msg = symb + msg + end
        cprint(msg, colors["ERROR"])

    elif msg_type == "EXCEPTION":
        symb = "[*] - "
        if exception_obj:
            # displays the exception name.
            _msg = symb + exception_obj["name"] + end
            cprint(_msg, colors["EXCEPTION"])
            # display message of the exception.
            _msg = symb + exception_obj["msg"] + end
            cprint(_msg, colors["EXCEPTION"])
            # show stack trace of exception.
            _msg = symb + exception_obj["traceback"] + end
            cprint(_msg, colors["EXCEPTION"])
        else:
            msg = symb + msg + end
            cprint(msg, colors["EXCEPTION"])

    elif msg_type == "DEBUG":
        from dotenv import load_dotenv
        load_dotenv()
        if os.getenv("DEV") == "True":
            symb = "[DEBUG] - "
            msg = symb + msg + end
            cprint(msg, colors["DEBUG"])

    else:
        symb = "[!] - "
        _msg = symb + "Argument error in print_msg() function. The argument is incorrect" + end
        cprint(_msg, colors["ERROR"])

        _msg = symb + f"msg_type = {msg_type}" + end
        cprint(_msg, colors["ERROR"])

        _msg = symb + f"msg = {msg}" + end
        cprint(_msg, colors["ERROR"])
        sys.exit()


# Allows you to create a typing animation on the text passed as a parameter.
# def typewriter(string, color="white"):
#     try:
#         string_to_array = list(string)
#         for index, char in enumerate(string_to_array):
#             if (index+1) == len(string_to_array):
#                 sys.stdout.write(colored(char + "\n", color))
#             else:
#                 sys.stdout.write(colored(char, color))
#             sys.stdout.flush()
#             time.sleep(0.002)

#     except KeyboardInterrupt:
#         sys.stdout.write("\n\n")
#         sys.stdout.flush()
#         print_msg("ERROR", "Stopping the script")
#         sys.exit()

#     except Exception as e:
#         sys.stdout.write("\n\n")
#         sys.stdout.flush()
#         print_msg("ERROR", "An error has occured")
#         print_msg("EXCEPTION", f"{e}")
#         sys.exit()


# Check the user's operating system.
def check_os():
    operating_system = platform.system().lower()
    if not operating_system == "windows":
        print_msg("ERROR", "Sorry, but this program currently only works on Windows.")
        print_msg("ERROR", "It appears that you are running this program on an unsupported platform.")
        print_msg("ERROR", "To run this program, please launch it on a Windows system.")
        sys.exit()


# Check the user's python version.
def check_python_version() :
    min_version = (3,9,7)
    user_version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    if sys.version_info < min_version:
        print_msg("ERROR", f"You are using an old version of python: {user_version}")
        print_msg("ERROR", "Please update to version 3.9.7 or higher")
        sys.exit()


# Check the values ​​of variables in the configuration file (config.py).
def check_config_values():
    ascii_text_animation = config.ASCII_TEXT_ANIMATION
    backup_file_name = config.BACKUP_FILE_NAME
    backup_active = config.BACKUP_ACTIVE

    if not isinstance(ascii_text_animation, bool):
        print_msg("ERROR", "The value of ASCII_TEXT_ANIMATIONof the config.py file  must be a boolean: True or False")
        print_msg("EXCEPTION", "Stopping the script")
        sys.exit()

    if not isinstance(backup_active, bool):
        print_msg("ERROR", "The value of BACKUP_ACTIVE of the config.py file must be a boolean: True or False")
        print_msg("EXCEPTION", "Stopping the script")
        sys.exit()

    if not isinstance(backup_file_name, str):
        print_msg("ERROR", "The value of BACKUP_FILE_NAME of the config.py file must be a character string")
        print_msg("EXCEPTION", "Stopping the script")
        sys.exit()
    else:
        regex = r"^(?![_-])(?!.*[_-]$)(?!.*__)[a-zA-Z]+(?:[-_][a-zA-Z]+)*$"
        if not re.match(regex, backup_file_name):
            print_msg("ERROR", "The value of BACKUP_FILE_NAME of the config.py file must be a character string containing only its characters: a-zA-Z.")
            print_msg("ERROR", "Hyphens and underscores are accepted but not at the beginning and end of the string.")
            print_msg("EXCEPTION", "Stopping the script")
            sys.exit()