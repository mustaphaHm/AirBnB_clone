# Project Name :
AirBnB Clone
## Project Description :
The project consist of deploying simple copy of the AirBnB website on our server.
## Command line interpreter Description :
Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:
   - Create a new object (ex: a new User or a new Place)
   - Retrieve an object from a file, a database etc…
   - Do operations on objects (count, compute stats, etc…)
   - Update attributes of an object
   - Destroy an object
## How to start a command line interpreter :
python3 filename.py
(Cmd)
## Simple Example :
import cmd


class HelloWorld(cmd.Cmd):

    def do_greet(self, line):
        print("hello")

    def do_EOF(self, line):
        return True


if __name__ == '__main__':
    HelloWorld().cmdloop()
## How to use It :
(Cmd) greet
hello
