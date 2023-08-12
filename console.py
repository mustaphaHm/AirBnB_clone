#!/usr/bin/python3
"""This is console mudole."""
import cmd


class HBNBCommand(cmd.Cmd):
    """Definition of class HBNBCommand."""

    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit to exit the program."""
        return True

    def do_EOF(self, line):
        """EOF to exit the program."""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
