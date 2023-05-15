#!/usr/bin/python3

import cmd
import sys

class HBNBCommand(cmd.Cmd):
    

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True
    def do_EOF(self, arg):
        """Handles End Of File character
        """
        return True

    def emptyline(self):
        """*** Unknown syntax: emptyline
        """
        pass
        """help :gives information into commands
        """



if __name__ == '__main__':
    """to work in non-interactive mode
    """
    if (len(sys.argv) > 1):
        HBNBCommand().onecmd("".join(sys.argv[1:]))
    else:
        HBNBCommand().cmdloop()
