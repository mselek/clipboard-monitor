import pyperclip
import random
from termcolor import cprint
####################
from backup import Backup
####################
import config
from utils import get_date, get_time
####################


class Clipboard:
    
    def __init__(self):
        self.backup = Backup()
        self.backup_active = config.BACKUP_ACTIVE
        self.colors = [
            "light_red",
            "light_green",
            "light_yellow",
            "light_cyan",
            "light_magenta",
        ]
        self.random_color = random.choice(self.colors)
        self.previous_color = None


    def wait_for_new_paste(self):
        new_paste = pyperclip.waitForNewPaste()
        new_paste = new_paste.strip()
        if not len(new_paste) == 0:
            # as long as the generated color is the same as the previous one, we continue to generate a new one.
            while self.random_color == self.previous_color:
                self.random_color = random.choice(self.colors)
            self.previous_color = self.random_color
            # if the backup is active, we write the new copied text in the backup file.
            if self.backup_active:
                self.backup.write_data(new_paste)
        # display copied text in terminal.
        cprint(f"___________[ {get_date()} - {get_time()} ]___________\n\n", self.random_color)
        print(new_paste + "\n\n")
        cprint("____________________[ END ]____________________" + "\n\n\n\n", self.random_color)