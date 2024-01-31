import os
####################
import config
from helpers import print_msg
from utils import get_date, get_time
####################


class Backup:

    def __init__(self):
        self.file_name = config.BACKUP_FILE_NAME
        self.file_ext = ".txt"
        self.backup_active = config.BACKUP_ACTIVE


    # Check if the backup file exists.
    def check_if_file_exists(self):
        return True if os.path.exists(self.file_name + self.file_ext) else False
    

    # Create the backup file.
    def create_file(self):
        with open(self.file_name + self.file_ext, "x") as file:
            pass


    # Writes data in backup file.
    def write_data(self, data):
        data = data.strip()
        with open(self.file_name + self.file_ext, "a+", encoding="utf-8") as file:
            file.write(f"___________[ {get_date()} - {get_time()} ]___________\n\n")
            file.write(data + "\n\n")
            file.write("____________________[ END ]____________________" + "\n\n\n\n")


    # When launching the script, this function will initialize the backup file.
    def initialization_of_the_backup_file(self):
        if self.backup_active:
            # check if backup file exists.
            if self.check_if_file_exists():
                print_msg("DEBUG", f"The backup file exists")
            else:
                print_msg("DEBUG", f"The PID was written to the LOCK file successfully")
                self.create_file()
            print_msg("INFO", f"The copied texts will be saved in the file {self.file_name + self.file_ext}")


    # def file_modification_detection(self):
    #     while True:
    #         # if not os.path.exists(self.file_name + self.file_ext):
    #         #     sys.exit("Le fichier à été supprimé")

    #         if not os.path.isfile(self.file_name + self.file_ext):
    #             print_msg("ERROR", f"The {self.file_name + self.file_ext} file cannot be found !")
    #             sys.exit()
    #         time.sleep(1)

