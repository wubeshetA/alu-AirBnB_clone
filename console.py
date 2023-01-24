#!/usr/bin/python3
"""console"""

import cmd
import sys
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

classes = {"BaseModel": BaseModel}


class HBNBCommand(cmd.Cmd):
    """Command processor for ALU-AirBnB project"""

    prompt = '(hbnb) '
    ruler = '-'

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
        print("Create command to create a new instance of a class")
        print("Usage: create <class name>")
        print("Example: create BaseModel")

    def do_show(self, cls_id, ):

        cls = cls_id.split(' ')[0]
        id = cls_id.split(' ')[1]

        storage = FileStorage()
        storage.reload()
        all_objects = storage.all()
        if not cls:
            print("** class name missing **")
        elif cls not in classes.keys():
            print("** class doesn't exist **")
        if not id:
            print("** instance id missing **")

        for obj_key in all_objects.keys():
            # obj_key is stored as follow:
            # Example: BaseModel.029307ba-43b9-476f-8856-55a800762378
            # so from the above string we need to get id

            # split the key into two parts to get the id.
            obj_id = obj_key.split('.')[1]
            # if user provided id and the id found here are the same, then that's the object the user is looking for.
            if obj_id == id:
                print(all_objects[obj_key])
                return
        # if we reach here, then the object is not found.
        print("** no instance found **")

    def help_show(self):
        print("Show command to print the string representation of an instance")
        print("Usage: show <class name> <id>")
        print("Example: show BaseModel 029307ba-43b9-476f-8856-55a800762378")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
