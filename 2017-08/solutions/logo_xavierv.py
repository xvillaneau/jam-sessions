#!/usr/bin/python3

"""
LOGO Interpreter for the Aug. 3rd 2017 PyATL Jam session
By Xavier Villaneau
Licensed under WTFPL - Do whatever the F- you want with it
"""

import turtle


# region Exceptions

class LOGOExit(Exception):
    """Exception raised when exiting the prompt"""
    pass


class LOGOUnknown(Exception):
    """Exception raised when a command is unknown"""
    pass


class LOGOInvalidInt(Exception):
    """Exception raised when a given argument is not an integer"""
    pass


def raise_exit():
    """Raise the Exception to quit the prompt"""
    raise LOGOExit

# endregion


# region Function utilities

def arg_to_int(func):
    """Decorator that converts the (supposedly unique) argument to an Int"""
    def _wrapped(str_arg):
        try:
            int_arg = int(str_arg)
        except ValueError:
            raise LOGOInvalidInt
        return func(int_arg)
    return _wrapped


def get_func(func_name):
    """Return a function that does stuff from"""

    # LOGO shortcuts
    expand = {
        "ST": "SHOWTURTLE",
        "PR": "PRINT",
        "CS": "CLEARSCREEN",
        "FD": "FORWARD",
        "BK": "BACK",
        "LT": "LEFT",
        "RT": "RIGHT",
    }

    # Actual function mappings
    funcs = {
        # Simple commands
        "SHOWTURTLE": turtle.showturtle,
        "CLEARSCREEN": turtle.clearscreen,
        "PRINT": print,
        "BYE": raise_exit,

        # Single-argument functions (expecting a number)
        "FORWARD": arg_to_int(turtle.forward),
        "BACK": arg_to_int(turtle.back),
        "LEFT": arg_to_int(turtle.left),
        "RIGHT": arg_to_int(turtle.right),
    }

    full_name = expand.get(func_name.upper(), func_name.upper())
    try:
        return funcs[full_name]
    except KeyError:
        raise LOGOUnknown

# endregion


# region Main procedures

def main_loop():
    """One iteration of the main loop"""

    raw_input = input("? ")
    cmd = raw_input.split()

    if not cmd:
        # Empty input: go to next
        return

    try:
        # Try to read the input command and run it
        func = get_func(cmd[0])
        func(*cmd[1:])

    except TypeError:
        print("INVALID ARGUMENTS")
        return
    except LOGOUnknown:
        print("I DON'T KNOW HOW TO {}".format(cmd[0].upper()))
        return
    except LOGOInvalidInt:
        print("THAT'S NOT A NUMBER")
        return


def main():
    """Main loop for the LOGO interpreter"""

    print("WELCOME TO LOGO")
    try:
        while True:
            main_loop()
    except (LOGOExit, KeyboardInterrupt, EOFError):
        print("\nGOODBYE")

# endregion

if __name__ == "__main__":
    main()
