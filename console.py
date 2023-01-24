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

    def do_show(self, cls_and_id):

        if len(cls_and_id) == 0:
            print("** class name missing **")
            return
        elif len(cls_and_id.split(' ')) == 1:
            print("** instance id missing **")
            return
        elif cls_and_id.split(' ')[0] not in classes.keys():
            print("** class doesn't exist **")
            return
        # create a key of the form <class name>.<id> to search in the storage
        user_key = cls_and_id.split(' ')[0] + '.' + cls_and_id.split(' ')[1]

        storage = FileStorage()
        storage.reload()
        all_objects = storage.all()

        # if the user input key is found in the storage, then print the object
        if user_key in all_objects.keys():
            print(all_objects[user_key])
            return

        # if we reach here, then the object is not found.
        print("** no instance found **")

    def help_show(self):
        print("Show command to print the string representation of an instance")
        print("Usage: show <class name> <id>")
        print("Example: show BaseModel 029307ba-43b9-476f-8856-55a800762378")

    def do_destroy(self, cls_and_id):

        if len(cls_and_id) == 0:
            print("** class name missing **")
            return
        elif len(cls_and_id.split(' ')) == 1:
            print("** instance id missing **")
            return
        elif cls_and_id.split(' ')[0] not in classes.keys():
            print("** class doesn't exist **")
            return
        # create a key of the form <class name>.<id> to search in the storage
        user_key = cls_and_id.split(' ')[0] + '.' + cls_and_id.split(' ')[1]

        storage = FileStorage()
        storage.reload()
        all_objects = storage.all()
        if user_key in all_objects.keys():
            del all_objects[user_key]
            storage.save()
            print("Object ", user_key, "has been destroyed successfully!")
            return
        # if we reach here, then the object is not found.
        print("** no instance found **")

    def help_destroy(self):
        print("Destroy command to delete an object from storage")
        print("Usage: destroy <class name> <id>")
        print("Example: destroy BaseModel 029307ba-43b9-476f-8856-55a800762378")

    # add shortcut for commands
    do_q = do_quit


if __name__ == '__main__':
    HBNBCommand().cmdloop()
