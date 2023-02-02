#!/usr/bin/python3
"""console"""

import cmd
from os import system
import sys
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
import re
# models class stored in dict for easier access.
classes = {
    "BaseModel": BaseModel,
    "User": User,
    "City": City,
    "Place": Place,
    "Review": Review,
    "State": State,
    "Amenity": Amenity
}


class HBNBCommand(cmd.Cmd):
    """Command processor for ALU-AirBnB project"""

    prompt = '(hbnb) '
    ruler = '-'

    def default(self, line):
        """default method for commands not in the cmd module.
        For this application it handles the dot notation commands."""

        if "." in line:

            command = line.split(".")
            if command[1] == "all()":
                self.do_all(command[0])

            elif command[1] == "count()":
                self.do_count(command[0])

            elif command[1].startswith("show("):
                self.do_show(command[0] + " " + command[1][6:-2])

            elif command[1].startswith("destroy("):
                self.do_destroy(command[0] + " " + command[1][9:-2])

            elif command[1].startswith("update("):

                # remove the model name, and get the rest of the string
                command_pattern = re.compile("update\\((.+)\\)")
                command_result = command_pattern.search(line).group()

                # get Id from the string
                id_pattern = re.compile(
                    "[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}"
                    "-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}"
                )

                id = id_pattern.search(command_result)
                if id is not None:
                    id = id.group()
                # check if attributes and values are provided in dict format
                dict_repr_pattern = re.compile(r"{.+}")
                dict_repr = dict_repr_pattern.search(line)

                # if it is dict format, execute update for each key value pair
                if dict_repr:

                    # get dict representation
                    dict_repr = dict_repr.group()
                    dict_repr = eval(dict_repr)

                    # excute the update with each key value pair
                    for key, value in dict_repr.items():
                        param_to_pass = command[0] + ' ' + \
                            str(id) + ' ' + key + ' ' + str(value)
                        self.do_update(param_to_pass)

                # if dict format is not provided, it means the attributes
                #  and values are provided as parameters
                else:

                    # get the parameters from the string
                    # and remove the first and last brackets
                    # the format of parms variable is as follows:
                    # ex: params:  "b1d6-eaaddf0e76c1", "first_name", "John"
                    # on the above line id value is trimmed for convenience.
                    params = command_result[7:-1]
                    # print("params: ", params)

                    # the following for loop is to check if user entered
                    # values with spaces after comma(,).
                    # If the user did not enter spaces after comma(,)
                    # it will create a problem while slicing the string to
                    # get the values, specifically value parameter is extracted
                    # without error given space is provided after comma(,).
                    index_counter = 0
                    for param in params.split(","):

                        if index_counter >= 1 and not param.startswith(" "):
                            print(
                                "Insert spaces after comma(,) "
                                "to divide parameters"
                            )
                            return
                        index_counter += 1

                    # get the id, attribute and value from the string
                    attr = params.split(",")[1][2:-1]
                    value = params.split(",")[2][1:]

                    # incase the value of variable value is int pass it on eval
                    # to convert it to int, if it is not int, it will throw an
                    # exception, in that case we will not pass it on eval.
                    try:
                        eval(value)
                        value = eval(value)
                    except Exception as e:
                        pass

                    # create the parameter string to pass on to do_update
                    param_to_pass = command[0] + ' ' + \
                        str(id) + ' ' + attr + ' ' + str(value)
                    self.do_update(param_to_pass)
            else:
                print("*** Unknown syntax: {}".format(line))
        else:
            print("*** Unknown syntax: {}".format(line))
    # basic commands

    def do_EOF(self, line):
        return True

    def do_quit(self, arg):
        return True
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

    # command to clear the window
    def do_clear(self, arg):
        system('cls')

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
            print("Destroyed successfully!")
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
            # print(args_len)
            # print(args_split)
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

    def do_count(self, cls):
        storage = FileStorage()
        storage.reload()
        all_objects = storage.all()
        if not cls:
            # Print all objects in the storage
            print(len([str(obj) for obj in all_objects.values()]))
            return
        elif cls not in classes.keys():
            print("** class doesn't exist **")
            return

        # If it reaches here, Print all objects of a specific class
        print(len([str(obj) for key, obj in all_objects.items()
                   if key.split('.')[0] == cls]))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
