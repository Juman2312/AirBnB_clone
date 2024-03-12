#!/usr/bin/python3
""" Defines the console class
which is the entry point of the Airbnb Project
"""


import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_help(self, arg):
        """Help command to display available commands"""
        if arg:
            cmd.Cmd.do_help(self, arg)
        else:
            print("Available commands:")
            print("- quit: Quit the program")
            print("- help: Display available commands")

if __name__ == '__main__':
    HBNBCommand().cmdloop()