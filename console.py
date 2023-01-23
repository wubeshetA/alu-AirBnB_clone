#!/usr/bin/python3
"""console"""

import cmd
import sys
from models.base_model import BaseModel

classes = {"BaseModel": BaseModel}


class HBNBCommand(cmd.Cmd):
    """Command processor for ALU-AirBnB project"""

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = '(hbnb) '

    # basic commands

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

    # commands to handle BaseModel

    def do_create(self, cls):
        if not cls:
            print("** class name missing **")
        elif cls not in classes.keys():
            print("** class doesn't exist **")
        else:
            new_model = classes[cls]()
            new_model.save()
            print(new_model.id)

    def help_create(self):
        print("\tCreate command to create a new instance of a class")
        print("\tUsage: create <class name>")
        print("\tExample: create BaseModel")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
