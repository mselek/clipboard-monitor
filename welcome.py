import sys
import random
import re
import time
from termcolor import colored
####################
import config
from helpers import print_msg
####################


class Welcome:

    def __init__(self):
        # Colors available : https://pypi.org/project/termcolor/
        self.colors = [
            "light_red",
            "light_green",
            "light_yellow",
            "light_cyan",
            "light_magenta",
            "white",
        ]
        self.ascii_text = [
            "\n",
            "\t+-+-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+",
            "\t|C|L|I|P|B|O|A|R|D| |M|O|N|I|T|O|R|",
            "\t+-+-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+",
            "\n",
            "\n"
        ]
        self.previous_color = None
        self.ascii_text_animation = config.ASCII_TEXT_ANIMATION


    def print_text(self):
        for array_elt in self.ascii_text:
            for index, char in enumerate(array_elt):
                # as long as the generated color is the same as the previous one, we continue to generate a new one.
                random_color = random.choice(self.colors)
                while random_color == self.previous_color:
                    random_color = random.choice(self.colors)
                self.previous_color = random_color
                try:
                    if re.match(r"[a-zA-Z]", char):
                        sys.stdout.write(colored(char, "light_green"))
                    else:
                        sys.stdout.write(colored(char, random_color))

                    if self.ascii_text_animation:
                        time.sleep(0.002)
                    sys.stdout.flush()

                    if (index+1) == len(array_elt):
                        print("")

                except KeyboardInterrupt:
                    sys.stdout.write("\n\n")
                    sys.stdout.flush()
                    print_msg("EXCEPTION", "Stopping the script")
                    sys.exit()

                except Exception as e:
                    sys.stdout.write("\n\n")
                    sys.stdout.flush()
                    import traceback
                    exception = {
                        "msg": str(e),
                        "traceback": traceback.format_exc(),
                        "name": type(e).__name__
                    }
                    print_msg("ERROR", "An error has occured !")
                    print_msg("EXCEPTION", exception_obj=exception)
                    sys.exit()
        time.sleep(0.5)