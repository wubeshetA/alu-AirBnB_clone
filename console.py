#!/usr/bin/python3
"""console"""

import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """Command processor for ALU-AirBnB project"""

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = '(hbnb) '

    def do_EOF(self, line):
        return True

    def do_quit(self, arg):
        sys.exit(1)

    def help_quit(self):
        print("Quit command to exit the program")

    def help_EOF(self):
        print("EOF command to exit the program")

    def help_help(self):
        print("Help command to print help information about a command")
    
    def emptyline(self):
        # do nothing
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
