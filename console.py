#!/usr/bin/python3
"""
==========================
    Base module for AirBnB
==========================
"""
import cmd
import sys


"""
=====================================
    create a class command line input
===================================== 
"""


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def __init__(self, args):
        super.__init__():

    def do_create(self, args):
        """Creates a new AirBnB object based on the argument"""

    def do_update(self, args):
        """Update an existing object"""

    def do_delete(self, args):
        """delete an existing object"""

    def do_show(self, args):
        """show the details of an object"""

    def do_EOF(self, args):
        """End of files"""
        return True

    def do_help(self, args):
        """Help documentation"""
        
        cmd.Cmd.do_help(self, args)
        
    def do_quit(self, args):
        """quit the interpreter"""
        return True

    def emptyline(self):
        """returns the empty line"""
        # return super().emptyline()
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()