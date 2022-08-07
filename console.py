#!/usr/bin/python3
"""
This is the entry to command interpreter
"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """
    Entry to command interpreter
    """

    prompt = "(hbnb)"  # this is a public instance variable from cmd
    classes = {"Amenity", "BaseModel", "City", "Place",
               "Review", "State", "User"}

    def do_EOF(self, line):
        """Exits after receiving the EOF signal"""
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def emptyline(self):
        """Overwrite default behavious to repeat it last cmd"""
        pass

    def do_create(self, line):
        """Creates a new instance of class specified by the user
        and prints its id
        """
        if len(line) == 0:
            print("** class name missing **")
        elif line not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            instance = eval(line)()
            instance.save()
            print(instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance based
        on the class name and id
        """
        new_storage = storage.all()
        response = validateInstance(line, new_storage)

        if (((isinstance(response[0], bool)) and response[0] is False)
                and isinstance(response[1], str)):
            print(response[1])  # this would mean error
            return
        else:
            value = new_storage[response[1]]  # this would be the name
            print(value)

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        new_storage = storage.all()
        response = validateInstance(line, new_storage)

        if (((isinstance(response[0], bool)) and response[0] is False)
                and isinstance(response[1], str)):
            print(response[1])  # this would mean error
            return
        else:
            del new_storage[response[1]]  # del the instance from storage
            storage.save()

    def do_all(self, line):
        """This prints all string representation of all instances
        based or not on the class name
        """
        args = parse(line)
        obj_list = []
        if len(line) == 0:
            for objs in storage.all().values():
                obj_list.append(objs)
            print(obj_list)
        elif args[0] in HBNBCommand.classes:
            for key, objs in storage.all().items():
                if args[0] in key:
                    obj_list.append(objs)
            print(obj_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Updates an instance based on the class name
        and id by adding or updating attribute
        """
        args = parse(line)
        new_storage = storage.all()
        if len(args) >= 4:
            key = "{}.{}".format(args[0], args[1])
            attr_cast = type(eval(args[3]))
            arg3 = args[3]
            arg3 = arg3.strip('"')
            arg3 = arg3.strip("'")
            setattr(new_storage[key], args[2], attr_cast(arg3))
            new_storage[key].save()
        elif len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif ("{}.{}".format(args[0], args[1])) not in new_storage.keys():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        else:
            print("** value missing **")
        new_storage = {}


def parse(line):
    """A helper method to parse user typed input
    on the cmd line
    """
    return tuple(line.split())


def validateInstance(line, obj_dict):
    """A helper method to validate users typed input on
    the cmd line
    """
    if len(line) == 0:
        return False, "** class name missing **"
    args = parse(line)
    if args[0] not in HBNBCommand.classes:
        return False, "** class doesn't exist **"
    try:
        if args[1]:
            name = "{}.{}".format(args[0], args[1])
            # since obj_dict was passed from models, it has been
            # reloaded already in the magic file __init__.py
            try:
                value = obj_dict[name]
                return True, name
            except KeyError:
                return False, "** no instance found **"
    except IndexError:
        return False, "** instance id missing **"


if __name__ == "__main__":
    HBNBCommand().cmdloop()
