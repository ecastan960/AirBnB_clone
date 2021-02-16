#!/usr/bin/python3
"""[summary]

Returns:
    [type]: [description]
"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.state import State
from models import storage
import inspect
import sys


class HBNBCommand(cmd.Cmd):
    """Simple command processor example."""
    prompt = '(hbnb)'
    y = inspect.getmembers(sys.modules[__name__], inspect.isclass)
    clases = [command[0] for command in y]

    def do_EOF(self, line):
        """EOF command to exit the program

        Args:
            line ([type]): [description]

        Returns:
            [type]: [description]
        """
        return True

    def do_quit(self, line):
        """Quit command to exit the program

        Args:
            line ([type]): [description]

        Returns:
            [type]: [description]
        """
        return True

    def emptyline(self):
        pass

    def do_create(self, *args, **kwargs):
        if len(args[0]) <= 0:
            print("** class name missing **")
        else:
            if args[0] in self.clases:
                x = eval(str(args[0])+'()')
                x.save()
                print(x.id)
            else:
                print("** class doesn't exist **")

    def do_show(self, *args):
        objs = storage.all()
        tokens = args[0].split()

        if len(tokens) > 1:
            name = str(tokens[0]) + "." + str(tokens[1])

        if len(tokens) == 0:
            print("** class name missing **")
        elif tokens[0] not in self.clases:
            print("** class doesn't exist **")
        elif len(tokens) == 1:
            print("** instance id missing **")
        elif name not in objs:
            print("** no instance found **")
        else:
            print(objs[name])

    def do_destroy(self, *args):
        objs = storage.all()
        tokens = args[0].split()

        if len(tokens) > 1:
            name = str(tokens[0]) + "." + str(tokens[1])

        if len(tokens) == 0:
            print("** class name missing **")
        elif tokens[0] not in self.clases:
            print("** class doesn't exist **")
        elif len(tokens) == 1:
            print("** instance id missing **")
        elif name not in objs:
            print("** no instance found **")
        else:
            objs.pop(name)
            storage.save()

    def do_all(self, *args):
        objs = storage.all()
        tokens = args[0].split()

        if len(tokens) > 0 and tokens[0] not in self.clases:
            print("** class doesn't exist **")
        elif len(tokens) == 1 and tokens[0] in self.clases:
            aux = []
            for key in objs:
                lookUpClass = key.split('.')
                if lookUpClass[0] == tokens[0]:
                    aux.append(str(objs[key]))
            print(aux)
        elif len(tokens) == 0:
            aux = [str(objs[element]) for element in objs]
            print(aux)

    def do_update(self, *args):
        objs = storage.all()
        tokens = args[0].split()

        if len(tokens) > 1:
            name = str(tokens[0]) + "." + str(tokens[1])
        if len(tokens) == 0:
            print("** class name missing **")
        elif len(tokens) > 0 and tokens[0] not in self.clases:
            print("** class doesn't exist **")
        elif len(tokens) == 1:
            print("** instance id missing **")
        elif name not in objs:
            print("** no instance found **")
        elif len(tokens) == 2:
            print("** attribute name missing **")
        elif len(tokens) == 3:
            print("** value missing **")
        elif name in objs:
            setattr(objs[name], tokens[2], tokens[3])
            objs[name].save()


if __name__ == '__main__':

    HBNBCommand().cmdloop()
