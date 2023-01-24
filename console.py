#!/usr/bin/python3
"""console"""

import cmd
import sys
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage

classes = {"BaseModel": BaseModel, "User": User}


class HBNBCommand(cmd.Cmd):
    """Command processor for ALU-AirBnB project"""

    prompt = '(hbnb) '
    ruler = '-'

    # basic commands

    def do_EOF(self, line):
        return True

    def do_quit(self, arg):
        sys.exit(1)
    # short cut for quit command.
    do_q = do_quit

    def help_q(self):
        print("Shortcut for quit command")

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

        # if the user input key is found in the storage, then delete the object
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
        print("Example: destroy BaseModel 029307ba-43b9-476f-55a800762378")

    def do_all(self, cls):
        storage = FileStorage()
        storage.reload()
        all_objects = storage.all()
        if not cls:
            print([str(obj) for obj in all_objects.values()])
        elif cls not in classes.keys():
            print("** class doesn't exist **")
        else:
            print([str(obj) for key, obj in all_objects.items()
                   if key.split('.')[0] == cls])

    def help_all(self):
        print(
            "All command to print all string representation of all instances"
        )
        print("Usage: all or all <class name>")
        print("Example: all")
        print("Example: all BaseModel")

    def do_update(self, args):

        args_split = args.split(' ')

        if len(args_split) < 4:
            args_len = len(args_split)
            print(args_len)
            print(args_split)
            if not args:
                print("** class name missing **")
                return
            if args_len == 1:
                print("** instance id missing **")
                return
            if args_len == 2:
                print("** attribute name missing **")
                return
            if args_len == 3:
                print("** value missing **")
                return

        else:
            args_split = args_split[:4]

            cls_name = args_split[0]
            obj_id = args_split[1]
            attr_name = args_split[2]
            attr_value = args_split[3]

            storage = FileStorage()
            storage.reload()
            all_objects = storage.all()

            # create a key of the form <class name>.<id> to search in storage
            user_key = cls_name + '.' + obj_id

            if cls_name not in classes.keys():
                print("** class doesn't exist **")
                return
            if user_key not in all_objects.keys():
                print("** no instance found **")
                return

            # if we reach here, then the object is found and update it.
            obj = all_objects[user_key]
            setattr(obj, attr_name, attr_value)
            obj.save()

    def help_update(self):
        print("Update command to update an attribute of an object")
        print("Usage: update <class name> <id> <attr name> <attr value>")
        print(
            "Example: update BaseModel 55a800762378 email username@gmail.com"
        )


if __name__ == '__main__':
    HBNBCommand().cmdloop()
