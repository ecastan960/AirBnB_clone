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
        """[summary]
        """
        pass

    def do_create(self, *args, **kwargs):
        """[summary]
        """
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
        """[summary]
        """
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
        """[summary]
        """
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
        """[summary]
        """
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
        """[summary]
        """
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

    def do_count(self, *args):
        """[summary]
        """
        objs = storage.all()
        tokens = args[0].split()
        count = 0
        for keys in objs:
            cl = keys.split('.')
            if cl[0] == tokens[0]:
                count += 1
        print(count)

    def default(self, *args):
        """[summary]
        """
        tokens = args[0].split('.')
        check = tokens[1].split('(')

        if check[0] == "show" or check[0] == "destroy":
            check_id = check[1].split(')')
            check_id = check_id[0]
            check_id = check_id[1:len(check_id) - 1]
        elif check[0] == "update":
            check_info = check[1].split(')')
            check_info = check_info[0].split(',')
            check_id = check_info[0]
            check_id = check_id[1:len(check_id) - 1]
            check_att = check_info[1]
            check_att = check_att[1:len(check_att) - 1]
            check_value = check_info[2]
            check_value = check_value[1:len(check_value) - 1]
            up_arg = tokens[0]+' '+check_id+' '+check_att+' '+check_value

        if len(tokens) == 2:
            if tokens[0] in self.clases and tokens[1] == 'all()':
                self.do_all(tokens[0])
            if tokens[0] in self.clases and tokens[1] == 'count()':
                self.do_count(tokens[0])
            if tokens[0] in self.clases and check[0] == "show":
                self.do_show(tokens[0]+' '+check_id)
            if tokens[0] in self.clases and check[0] == "destroy":
                self.do_destroy(tokens[0]+' '+check_id)
            if tokens[0] in self.clases and check[0] == "update":
                self.do_update(up_arg)

if __name__ == '__main__':
    """[summary]
    """
    HBNBCommand().cmdloop()
