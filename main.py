import sys
import time
####################
from welcome import Welcome
from locking_mechanism import LockingMechanism
from backup import Backup
from clipboard import Clipboard
####################
from helpers import print_msg, check_os, check_python_version, check_config_values
from utils import display_active_backup_status, display_how_to_exit, display_copy_text_to_print_in_terminal
####################


def main() -> None:
    try:
        import os
        # command used to change text and background colors in the Windows console.
        os.system("color")
        # check the user's operating system.
        check_os()
        # check the user's python version.
        check_python_version()
        # check the values ​​of variables in the configuration file (config.py).
        check_config_values()

        # instantiation of imported classes.
        welcome = Welcome()
        locking_mechanism = LockingMechanism()
        backup = Backup()
        clipboard = Clipboard()

        # display ascii text.
        welcome.print_text()
        # the call to this function will set up the program locking mechanism, to avoid other instances of the program.
        locking_mechanism.initialization_of_the_locking_mechanism()
        # display active backup status.
        display_active_backup_status()
        # initialize the backup file.
        backup.initialization_of_the_backup_file()
        # display how to exit the program.
        display_how_to_exit()
        # display copy text to print.
        display_copy_text_to_print_in_terminal()
        
        #####################################
        # import threading
        # th1 = threading.Thread(target=backup.file_modification_detection)
        # th1.start()
        #####################################
        
        while True:
            clipboard.wait_for_new_paste()
            time.sleep(1)

    except KeyboardInterrupt:
        print_msg("EXCEPTION", "Stopping the script")
        sys.exit()

    except Exception as e:
        import traceback        
        exception = {
            "msg": str(e),
            "traceback": traceback.format_exc(),
            "name": type(e).__name__
        }
        print_msg("ERROR", "An error has occured !")
        print_msg("EXCEPTION", exception_obj=exception)
        sys.exit()

####################

if __name__ == '__main__':
    main()