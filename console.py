import cmd 
prompt = "(hbnb)"

class HBNBCommand(cmd.Cmd):
    def do_EOF(self, arg):
        """exit out of the program using CTRL D OR CTRL C"""
        return True

    def do_quit(self, arg):
        """terminates the program using the quit command"""
        return True
    def do_emptyline(self):
        pass
    def precmd(self, line):
        """makes the app to work in non-interactive mode"""
        if not sys.stdin.isatty():

