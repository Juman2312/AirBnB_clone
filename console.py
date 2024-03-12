#!/usr/bin/python3
""" Defines the console class
which is the entry point of the Airbnb Project
"""


import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    valid_classes = ['BaseModel', 'User']  # Add 'User' to the list of valid classes

    def do_create(self, arg):
        """Create a new instance of a class"""
        if not arg:
            print("** class name missing **")
            return
        arg = arg.split()
        class_name = arg[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return
        new_obj = eval(class_name)()
        new_obj.save()
        print(new_obj.id)

    def do_show(self, arg):
        """Show an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        arg = arg.split()
        class_name = arg[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return
        if len(arg) < 2:
            print("** instance id missing **")
            return
        obj_id = arg[1]
        key = class_name + "." + obj_id
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return
        print(all_objs[key])

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        arg = arg.split()
        class_name = arg[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return
        if len(arg) < 2:
            print("** instance id missing **")
            return
        obj_id = arg[1]
        key = class_name + "." + obj_id
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return
        del all_objs[key]
        storage.save()

    def do_update(self, arg):
        """Update an instance based on the class name, id, attribute, and value"""
        if not arg:
            print("** class name missing **")
            return
        arg = arg.split()
        class_name = arg[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return
        if len(arg) < 2:
            print("** instance id missing **")
            return
        obj_id = arg[1]
        key = class_name + "." + obj_id
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return
        if len(arg) < 3:
            print("** attribute name missing **")
            return
        if len(arg) < 4:
            print("** value missing **")
            return
        attribute = arg[2]
        value = arg[3]
        obj = all_objs[key]
        setattr(obj, attribute, value)
        obj.save()

    def do_all(self, arg):
        """Print all string representations of all instances"""
        all_objs = storage.all()
        print([str(obj) for obj in all_objs.values()])


    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Quit command to exit the program"""
        print("")
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def postloop(self):
        """Print a new line after exiting the command interpreter"""
        print()

    def do_help(self, arg):
        """Help command to display available commands"""
        if arg:
            cmd.Cmd.do_help(self, arg)
        else:
            print("Documented commands (type help <topic>):")
            print("- quit: Quit the program")
            print("- help: Display available commands")

if __name__ == '__main__':
    HBNBCommand().cmdloop()