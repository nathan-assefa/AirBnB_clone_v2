#!/usr/bin/python3
""" Implementing console from cmd module """


import cmd
from models import storage
from models.base_model import BaseModel


class_names = {
    "BaseModel": BaseModel
    # User,
    # Amenity,
    # State,
    # City,
    # Place,
    # Review,
}


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_create(self, arg):
        """We need to use try and except block to handle any
        unexpected errors that may occur while creating and
        saving a new instance of the BaseModel. For example, if there
        is an error in the way we're calling the BaseModel constructor,
        the program may crash with an error message that doesn't provide
        much information about what went wrong. By using a try-except block,
        we can catch and handle such errors in a more graceful way,
        e.g., by printing an informative error message to the user.
        """

        try:
            args = arg.split()

            if not args:
                print("** class name missing **")
                return
            elif args[0] not in class_names:
                print("** class doesn't exist **")
                return
            new_inst = class_names[args[0]]()
            new_inst.save()
            print(new_inst.id)
        except Exception as e:
            print(e)

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on
        the class name and id. Ex: $ show BaseModel 1234-1234-1234.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        elif args[0] not in class_names:
            print("** class doesn't exist **")
            return

        elif len(args) < 2:
            print("** instance id missing **")
            return
        try:
            objects = storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key not in objects:
                print("** no instance found **")
            else:
                print(objects[key])
        except Exception as e:
            print(e)

    def do_destroy(self, arg):
        args = arg.split()
        try:
            if not args:
                print("** class name missing **")
                return
            elif args[0] not in class_names:
                print("** class doesn't exist **")
                return
            elif len(args) < 2:
                print("** instance id missing **")
                return
            objects = storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key not in objects:
                print("** no instance found **")
                return
            else:
                del objects[key]
        except Exception as e:
            print(e)

    def do_all(self, arg):
        """Prints all the instances"""
        try:
            args = arg.split()
            objects = storage.all()
            # let us first check if the class if a class name exists
            if args and args[0] not in class_names:
                print("** class doesn't exist **")
                return
            if args:
                new_obj = [
                    str(obj)
                    for obj in objects.values()
                    if args[0] == type(obj).__name__
                ]
            elif len(args) == 0:
                new_obj = [str(obj) for obj in objects.values()]

            print(new_obj)

        except Exception as e:
            print(e)

    def do_update(self, arg):
        """updating an instance"""
        args = arg.split()
        try:
            if not args:
                print("** class name missing **")
                return
            elif args[0] not in class_names:
                print("** class doesn't exist **")
                return
            elif len(args[1]) < 2:
                print("** instance id missing **")
                return

            elif len(args) < 3:
                print("** attribute name missing **")
                return
            elif len(args) < 4:
                print("** value missing **")
                return

            key = "{}.{}".format(args[0], args[1])

            objects = storage.all()
            if key not in objects.keys():
                print("** no instance found **")
                return

            import ast

            attr_name = args[2]

            if attr_name in ["id", "created_at", "updated_at"]:
                return

            attr_val_str = args[3]

            try:
                attr_val = ast.literal_eval(attr_val_str)
                """ Here we can also use attr_val = eval(attr_val_str), but
                ast_literal_eval() is more secure since it only evaluets literal
                data types, namely, str, int, float etc...
                """
                """
                For security sake we have to use type(getattr(ins, key, val)) to,
                which is explained at the bottom, identify the data type of an object
                """
            except ValueError:
                # Handle the case where the attribute value is not a literal
                attr_val = attr_val_str

            setattr(objects[key], attr_name, attr_val)
            objects[key].save()
            """ Optionally we can use this code too
            instance = objects[key]
            attr_name = args[2]

            if attr_name in ['id', 'created_at', 'updated_at']:
                return

            attr_value = args[3]
            attr_type = type(getattr(instance, attr_name))
            setattr(instance, attr_name, attr_type(attr_value))
            storage.save()

            -> The line of code, attr_type = type(getattr
            (instance, attr_name)) or eval(attr_name), gets the type of the attribute value
            that was just retrieved using getattr(). This is necessary
            because we need to cast the new attribute value, attr_value,
            to the same type as the original attribute value before
            we can set it using setattr()
            """

            ''' Additionally, we can also use 'update' function to add and modify attribute
            attr_name = args[2]
            attr_val = args[3]
            try:
                attr_val = eval(attr_val)
            except:
                pass

            obj = objects[key]
            obj_dict = obj.to_dict()
            obj_dict[attr_name] = attr_val
            obj.update(obj_dict)
            storage.save()
            '''

        except Exception as e:
            print(e)

    def do_EOF(self, arg):
        print()
        return True

    def do_quit(self, arg):
        return True

    def do_exit(self, arg):
        return True

    def emptyline(self):
        pass

    def help_quit(self):
        print("Usage: quit")
        print("Quit command to exit the program")

    def help_EOF(self):
        print("Usage: EOF")
        print("EOF command to exit the program")

    def help_exit(self):
        print("Usage: exit")
        print("Exit command to exit the program")

    def help_create(self):
        print("Usage: create")
        print("Create command to create an instance")

    def help_show(self):
        print("usage: show")
        print("Show command to show instances")

    def help_destroy(self):
        print("Usage: show")
        print("Destroy command to delete a specific instance from the file")

    def help_all(self):
        print("Usage: all")
        print("All command Prints all string representation of all instances")
        print("based or not on the class name. Ex: $ all BaseModel or $ all.")

    def help_update(self):
        print("Usage: update")
        print("Update command Updates an instance based on the class name")
        print("and id by adding or updating attribut(save the change into")
        print("the JSON file)")
        print("Ex: $ update BaseModel 1234-1234-1234 email 'aibnb@mail.com'.")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
