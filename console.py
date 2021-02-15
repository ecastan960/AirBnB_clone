#!/usr/bin/python3
"""[summary]

Returns:
    [type]: [description]
"""

import cmd
from models.base_model import *
import inspect
import sys
class HBNBCommand(cmd.Cmd):
    """Simple command processor example."""
    prompt = '(hbnb)'

    def do_greet(self, line):
        """[summary]

        Args:
            line ([type]): [description]
        """
        print("hello")

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
            y = inspect.getmembers(sys.modules[__name__], inspect.isclass)
            # print(type(y))
            # print(y[0][0])
            # print (inspect.getmembers(sys.modules[__name__], inspect.isclass))
            clases = [command[0] for command in y]
            # print(clases)
            if args[0] in clases:
                x = eval(str(args[0])+'()')
                print(x)
            else:
                print("** class doesn't exist **")
            # print(x)
            # print(self.__dict__)

if __name__ == '__main__':

    HBNBCommand().cmdloop()
