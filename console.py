#!/usr/bin/python3
"""This is console module."""
import cmd
import re
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """Definition of class HBNBCommand."""

    prompt = "(hbnb) "
    classes = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review
    }

    def do_quit(self, line):
        """Quit to exit the program."""
        return True

    def do_EOF(self, line):
        """EOF to exit the program."""
        return True

    def emptyline(self):
        """Do nothing when it's an empty line."""
        pass

    def default(self, line):
        """Hundle when user type <class name>.<method name>()."""
        commands = {
            "create": self.do_create,
            "show": self.do_show,
            "all": self.do_all,
            "destroy": self.do_destroy,
            "update": self.do_update,
            "count": self.do_count,
        }

        split_parts = re.split(r'(\(|\)|\s|\.|\,)', line)
        split_parts = [part for part in split_parts if part.strip() != '']

        if len(split_parts) >= 3:
            class_name = split_parts[0]
            command = split_parts[2]

        if class_name in HBNBCommand.classes and command in commands:
            if len(split_parts) > 4:
                argument = split_parts[4].strip("(')")
                commands[command](class_name + ' ' + argument)
            else:
                commands[command](class_name)
            return

        print("*** Unknown syntax:", line)

    def validate_class_and_id(self, line):
        """Validate class name and instance ID."""
        if not line:
            print("** class name missing **")
            return None, None

        args = line.split()
        class_name = args[0]
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return None, None

        if len(args) < 2:
            print("** instance id missing **")
            return None, None

        obj_dict = models.storage.all()
        key = class_name + "." + args[1]
        if key not in obj_dict:
            print("** no instance found **")
            return None, None

        return class_name, key

    def do_create(self, line):
        """Create a new instance of BaseModel."""
        if not line:
            print("** class name missing **")
            return
        class_name = line.split()[0]
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        new_instance = HBNBCommand.classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, line):
        """Print the string representation of an instance."""
        class_name, key = self.validate_class_and_id(line)
        if class_name and key:
            print(models.storage.all()[key])

    def do_destroy(self, line):
        """Delete an instance by id."""
        class_name, key = self.validate_class_and_id(line)
        if class_name and key:
            del models.storage.all()[key]
            models.storage.save()

    def do_all(self, line):
        """Print all string representation of all instances."""
        obj_list = []
        if not line:
            for key, obj in models.storage.all().items():
                obj_list.append(str(obj))
            print(obj_list)
        else:
            class_name = line.split()[0]
            if class_name not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            for key, obj in models.storage.all().items():
                if class_name in key:
                    obj_list.append(str(obj))
            print(obj_list)

    def do_update(self, line):
        """Update an instance based on the class name and id."""
        class_name, key = self.validate_class_and_id(line)
        if class_name is None or key is None:
            return
        if class_name and key:
            args = line.split()
        if len(args) < 3:
            print("** attribute name missing **")
            return
        attr_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return
        attr_value = ' '.join(args[3:])

        # Remove surrounding double quotes from attribute value
        if attr_value.startswith('"') and attr_value.endswith('"'):
            attr_value = attr_value[1:-1]
        elif attr_value.startswith('[') and attr_value.endswith(']'):
            attr_value = attr_value[1:-1]
        elif attr_value.startswith('{') and attr_value.endswith('}'):
            attr_value = attr_value[1:-1]

        obj_dict = models.storage.all()
        instance = obj_dict[key]
        if hasattr(instance, attr_name):
            setattr(instance, attr_name, attr_value)
            instance.save()
        else:
            setattr(instance, attr_name, attr_value)
            instance.save()

    def do_count(self, line):
        """Retrieve the number of instances of a class."""
        lenght = 0
        cls_name = line.strip()
        if cls_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        for key, obj in models.storage.all().items():
            if cls_name in key:
                lenght += 1
        print(lenght)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
