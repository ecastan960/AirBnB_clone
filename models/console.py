#!/usr/bin/python3
"""[summary]

Returns:
    [type]: [description]
"""
import cmd


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

if __name__ == '__main__':

    HBNBCommand().cmdloop()
