#!/usr/bin/python3

"""Entry point of the command interpreter"""


import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage
import shlex
from datetime import datetime


class HBNBCommand(cmd.Cmd):
    """HBNB class"""
    prompt = '(hbnb) '
    __classes = ["BaseModel", "User",
                 "State", "City",
                 "Amenity", "Place", "Review"]

    def do_create(self, line):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file), and prints the id."""

        list_args = line.split()
        class_name = list_args[0]
        if not list_args:
            """checks If the class name is missing"""
            print("** class name missing **")
            return
        elif class_name not in HBNBCommand.__classes:
            """checks If the class name doesn't exist"""
            print("** class doesn't exist **")
            return
        else:
            """creates new instance of base model"""
            print(eval(class_name)().id)
            storage.save()
            return

    def do_show(self, line):
        """Prints the string representation of an
        instance by its class name and id
        """
        list_args = line.split()
        class_name = list_args[0]
        if not list_args:
            """checks If the class name is missing"""
            print("** class name missing **")
            return
        elif class_name not in HBNBCommand.__classes:
            """checks If the class name doesn't exist"""
            print("** class doesn't exist **")
            return
        else:
            """checks If the id is missing"""
            if len(list_args) >= 2:
                class_id = "{}.{}".format(list_args[0], str(list_args[1]))
                objects = storage.all()
                if class_id in objects.keys():
                    print(objects[class_id])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")

    def do_destroy(self, line):
        """Deletes an instance from memory
          by its class name and id"""
        list_args = line.split()
        class_name = list_args[0]
        if not list_args:
            """checks If the class name is missing"""
            print("** class name missing **")
            return
        elif class_name not in HBNBCommand.__classes:
            """checks If the class name doesn't exist"""
            print("** class doesn't exist **")
            return
        else:
            """checks If the id is missing"""
            if len(list_args) >= 2:
                class_id = "{}.{}".format(list_args[0], str(list_args[1]))
                objects = storage.all()
                if class_id in objects.keys():
                    del objects[class_id]
                    storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")

    def do_all(self, line):
        """
        Prints all string representation of all instances
        based on the class name
        """
        objects = storage.all()
        if line:
            list_args = line.split()
            if list_args[0] in HBNBCommand.__classes:
                class_objs = [
                    str(v) for k, v in objects.items()
                    if list_args[0] == k.split('.')[0]
                    ]
                print(class_objs)
            else:
                print("** class doesn't exist **")
        else:
            allObjs = [str(v) for k, v in objects.items()]
            print(allObjs)

    def do_update(self, line):
        """
        Updates an instance based on the class name
        and id by adding or updating attribute
        """
        the_dict = storage.all()
        cmd, arg, _ = self.parseline(line)
        if cmd is None:
            print("** class name missing **")
            return
        elif cmd not in self.__classes:
            print("** class doesn't exist **")
            return
        elif arg == "" or arg is None:
            print("** instance id missing **")
            return
        l_arg = shlex.split(arg)
        """print("{}".format(arg))"""
        b = "{}.{}".format(cmd, l_arg[0])
        a = the_dict.get(b)
        if a:
            if len(l_arg) < 2:
                print("** attribute name missing **")
            elif len(l_arg) < 3:
                print("** value missing **")
            else:
                if l_arg[1] not in b.__class__.__dict__.keys():
                    setattr(a, l_arg[1], l_arg[2].strip())
                else:
                    t = type(b.__class__.__dict__[l_arg[1]])
                    setattr(a, l_arg[1], t(l_arg[2].strip()))
                setattr(a, 'updated_at', datetime.now())
                storage.save()
        else:
            print("** no instance found **")

    def do_quit(self, line):
        """Exit the interpreter"""
        return True

    def do_EOF(self, line):
        """exits the program"""
        print("")
        return True

    def help_quit(self):
        """Help message for quit command."""
        print("Quit command to exit the program")

    def emptyline(self):
        """Empty line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
