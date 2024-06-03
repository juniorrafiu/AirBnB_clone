import cmd
from models.base_model import BaseModel

"""
This module defines the HBNBCommand class, which provides a command-line
interface for creating, managing, and interacting with BaseModel instances.
"""


class HBNBCommand(cmd.Cmd):
    """HBNB class"""
    prompt = "(hbnb)"
    __classes = {'BaseModel': BaseModel}

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return
        if arg not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        new_instance = HBNBCommand.__classes[arg]()
        new_instance.save()
        print(new_instance.id)

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
