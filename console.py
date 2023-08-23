import cmd
import models

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        return True

    def emptyline(self):
        """Do nothing on empty input"""
        pass

    def do_create(self, arg):
        """Create a new instance of a class"""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Print the string representation of an instance"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if len(args) < 2:
            print("** instance id missing **")
            return

        try:
            cls_name = args[0]
            obj_id = args[1]
            obj = models.storage.find(cls_name, obj_id)
            if obj and cls_name == "User":
                print(obj)
            elif obj and cls_name != "User":
                print("** class doesn't exist **")
            else:
                print("** no instance found **")
        except IndexError:
            if not args:
                print("** class name missing **")
            else:
                print("** instance id missing **")
        except NameError:
            print("** class doesn't exist **")
        def do_destroy(self, arg):
            """Delete an instance based on the class name and id"""
            args = arg.split()
            if not args:
                print("** class name missing **")
                return
            try:
                cls_name = args[0]
                obj_id = args[1]
                obj = models.storage.find(cls_name, obj_id)
                if obj:
                    models.storage.delete(obj)
                    models.storage.save()
                else:
                    print("** no instance found **")
            except IndexError:
                if not args:
                    print("** class name missing **")
                else:
                    print("** instance id missing **")
            except NameError:
                print("** class doesn't exist **")

    def do_all(self, arg):
        """Print all string representations of all instances"""
        args = arg.split()
        objects = models.storage.all()
        if not args:
            print([str(obj) for obj in objects.values()])
        else:
            try:
                cls_name = args[0]
                if cls_name in models.classes:
                    print([str(obj) for obj in objects.values() if type(obj).__name__ == cls_name])
                else:
                    print("** class doesn't exist **")
            except NameError:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """Update an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            cls_name = args[0]
            obj_id = args[1]
            obj = models.storage.find(cls_name, obj_id)
            if obj:
                if len(args) > 2:
                    attr_name = args[2].strip("\"")
                    if len(args) > 3:
                        attr_value = args[3].strip("\"")
                        attr_type = type(getattr(obj, attr_name))
                        setattr(obj, attr_name, attr_type(attr_value))
                        obj.save()
                else:
                    print("** attribute name missing **")
            else:
                print("** no instance found **")
        except IndexError:
            if not args:
                print("** class name missing **")
            elif len(args) == 1:
                print("** instance id missing **")
            else:
                print("** attribute value missing **")
        except NameError:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()