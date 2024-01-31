import os
import sys
####################
from helpers import print_msg
####################


# inspired by https://github.com/r3ap3rpy/python/blob/master/custom_app.py
class LockingMechanism:

    def __init__(self):
        # get the root directory of the project.
        self.cwd = os.getcwd()
        # constructing the path to the LOCK file.
        self.file_name = os.path.join(self.cwd, "LOCK")
        # obtaining the PID of the current process.
        self.pid = os.getpid()


    # Check if the "LOCK" file exists.
    def check_if_file_exists(self):
        return True if os.path.isfile(self.file_name) else False


    # Used to obtain the contents of the "LOCK" file. Must contain an integer (PID).
    def get_old_pid(self):
        try:
            if not os.path.getsize(self.file_name) == 0:
                with open(self.file_name, "r") as file_name:
                    old_pid = int(file_name.read())
                    return old_pid
            else:
                pass

        except Exception:
            print_msg("ERROR", "An error has occured")
            print_msg("EXCEPTION", "The pid written in the LOCK file is not an integer")
            sys.exit()


    # Return the running PIDS.
    def get_running_pids(self):
        # this command will retrieve the list of PIDS.
        output = os.popen('wmic process get processid').read()
        # separate the output into lines.
        lines = output.strip().split('\n')
        # initialize a list to store PIDS.
        pids = []
        # loop through each line of the output.
        for line in lines:
            # try to convert the line to an integer (PID).
            try:
                pid = int(line.strip())
                pids.append(pid)

            except ValueError:
                pass
        return pids


    # Check if the program PID is already running.
    def script_already_running(self):
        old_pid = self.get_old_pid()
        running_pids = self.get_running_pids()
        return True if old_pid in running_pids else False


    # Create the LOCK file.
    def create_file(self):
        with open(self.file_name, "x") as file_name:
            pass


    # Write the program PID to the LOCK file.
    def write_pid(self):
        with open(self.file_name, "w") as file_name:
            file_name.write(str(self.pid))


    # When the script is launched, this function will be responsible for initializing the program's locking mechanism.
    def initialization_of_the_locking_mechanism(self):
        # check if LOCK file exists.
        if  self.check_if_file_exists():
            print_msg("DEBUG", "The LOCK file exists")
            # check if the old pid is running.
            if self.script_already_running():
                print_msg("DEBUG", f"OLDPID : {self.get_old_pid()}")
                print_msg("DEBUG", f"PID : {self.pid}")
                print_msg("ERROR", f"The script is already running (PID : {self.get_old_pid()})")
                sys.exit()
            else:
                print_msg("DEBUG", f"OLDPID : {self.get_old_pid()}")
                print_msg("DEBUG", f"PID : {self.pid}")
                # write the PID of the program in the LOCK file.
                self.write_pid()
                print_msg("DEBUG", "The PID was written to the LOCK file")
        else:
            print_msg("DEBUG", "The LOCK file does not exists")
            # the file does not exist, we create it.
            self.create_file()
            print_msg("DEBUG", "The LOCK file has been created")
            # write the PID inside the LOCK file.
            self.write_pid()
            print_msg("DEBUG", "The PID was written to the LOCK file")
            print_msg("DEBUG", f"OLDPID : {self.get_old_pid()}")
            print_msg("DEBUG", f"PID : {self.pid}")