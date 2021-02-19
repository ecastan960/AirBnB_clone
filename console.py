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
import ast
import inspect
import json
import sys


class HBNBCommand(cmd.Cmd):
    """Simple command processor example."""
    prompt = '(hbnb) '
    y = inspect.getmembers(sys.modules[__name__], inspect.isclass)
    clases = [command[0] for command in y]

    def do_EOF(self, line):
        """EOF command to exit the program
        """
        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def emptyline(self):
        """Overwrite function to do nothing
        when press enter on an empty line
        """
        pass

    def do_create(self, *args, **kwargs):
        """Creates a new instance of the
        input class and prints the id of the
        new instance.
        Example on console-> create User
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
        """ Prints the string representation of
        an instance based on the class name and id
        Example on console-> show User 1234-12345-4562
        Example on console-> User.show("1234-12345-4562")
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
        """ Deletes an instance based on the class
        name and id
        Example on console-> destroy User 1234-12345-4562
        Example on console-> User.destroy("1234-12345-4562")
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
        """Prints all string representation of all
        instances based or not on the class name
        Example on console-> all
        Example on console-> all User
        Example on console-> User.all()
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
        """ Updates an instance based on the class name
        and id by adding or updating attribute (save the
        change into the JSON file)
        Example on console->update User 1234-1234
        email "aibnb@holbertonschool.com"
        Example on console->User.update("1234-1234",
        "first_name", "John"))
        Example on console->User.update("1234-1234",
        {'first_name': "John", "age": 89})
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
        flag_dict = 0

        if check[0] == "show" or check[0] == "destroy":
            check_id = check[1].split(')')
            check_id = check_id[0]
            check_id = check_id[1:len(check_id) - 1]
        elif check[0] == "update":
            check_info = check[1].split(')')
            check_dict = list(check_info[0].split(',', 1))
            check_dict = check_dict[1]
            check_dict = check_dict[1:]
            check_dict = ast.literal_eval(check_dict)
            if type(check_dict) is dict:
                flag_dict = 1
                check_info = check_info[0].split(',')
                check_id = check_info[0]
                check_id = check_id[1:len(check_id) - 1]
                for keys in check_dict:
                    check_att = keys
                    check_val = check_dict[keys]
                    check_val = str(check_val)
                    up_arg = tokens[0]+' '+check_id+' '+check_att+' '+check_val
                    if tokens[0] in self.clases and check[0] == "update":
                        self.do_update(up_arg)
            else:
                check_info = check_info[0].split(',')
                check_id = check_info[0]
                check_id = check_id[1:len(check_id) - 1]
                check_att = check_info[1]
                check_att = str(check_att)
                check_att = check_att.replace('"', '')
                check_val = check_info[2]
                check_val = str(check_val)
                check_val = check_val.replace('"', '')
                up_arg = tokens[0]+' '+check_id+' '+check_att+' '+check_val

        if len(tokens) == 2 and flag_dict == 0:
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
