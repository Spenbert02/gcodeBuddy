import sys
from gcodeBuddy.marlin import get_commands

"""
gcode_command object for ***MARLIN*** g-code flavor
"""

class Command:
    """
    Represents universal g-code command line
    """
    # Self notes for creating documentation:
    # initialization parameters: user_string
    # attributes: line_string, command, params
    # methods: get_command, has_param, get_param, get_string
    def __init__(self, init_string):
        """
        Initialization method
        """
        err_msg = "Error in marlin.gcode_command.__init__(): "
        legal_commands = get_commands()

        # removing extraneous spaces
        command_string = init_string
        while command_string[0] == " ":
            command_string = command_string[1:]
        while command_string[-1] == " ":
            command_string = command_string[:-1]
        ind = 0
        while (ind + 1) < len(command_string):
            if command_string[ind] == " " and command_string[ind + 1] == " ":
                command_string = command_string[:ind] + command_string[(ind + 1):]
            else:
                ind += 1

        # ensuring valid command
        command_list = command_string.split(" ")
        if command_list[0] in legal_commands:
            self.command = command_list[0]
            command_list = command_list[1:]
        else:
            print(err_msg + "Unrecognized Marlin command passed in argument 'init_string'")
            sys.exit(1)

        self.params = dict()
        for parameter_str in command_list:
            if parameter_str[0].isalpha():
                try:
                    float(parameter_str[1:])
                except ValueError:
                    print(err_msg + "Marlin parameter passed in argument 'init_string' of non-int/non-float type")
                    sys.exit(1)
                else:
                    self.params[parameter_str[0].upper()] = float(parameter_str[1:])
            else:
                print(err_msg + "Unrecognized Marlin parameter passed in argument 'init_string'")
                sys.exit(1)

    def get_command(self):
        """
        Returns Line instance's command as string
        """
        return self.command

    def has_param(self, param_char):
        """
        Returns True if line has given parameter, else returns False
        """
        err_msg = "Error in marlin.gcode_command.has_param(): "
        # ensuring string passed
        if isinstance(param_char, str):
            return param_char.upper() in self.params
        else:
            print(err_msg + "Argument 'param_char' of non-string type")
            sys.exit(1)

    def get_param(self, param_char):
        """
        Returns parameter value as float
        """
        err_msg = "Error in marlin.gcode_command.get_param(): "
        # ensuring param_char is string, and is in self.params
        if isinstance(param_char, str):
            if param_char in self.params:
                return self.params[param_char]
            else:
                print(err_msg + "Command does not contain Marlin parameter given in argument 'param_char'")
                sys.exit(1)
        else:
            print(err_msg + "Argument 'param_char' of non-string type")
            sys.exit(1)

    def set_param(self, param_char, param_val):
        """
        Sets given parameter character to given parameter value
        """
        err_msg = "Error in marlin.gcode_command.set_param(): "
        # ensuring param_char is string and is in self.params and param_val is number
        if isinstance(param_char, str):
            if isinstance(param_val, (int, float)):
                if param_char in self.params:
                    self.params[param_char] = param_val
                else:
                    print(err_msg + "Command does not contain Marlin parameter given in argument 'param_char'")
                    sys.exit(1)
            else:
                print(err_msg + "Argument 'param_val' of non-int/non-float type")
                sys.exit(1)
        else:
            print(err_msg + "Argument 'param_char' of non-string type")
            sys.exit(1)

    def get_string(self):
        """
        Returns entire command line as string
        """
        ret_val = self.command
        for param_key in self.params:
            ret_val += " " + param_key + str(self.params[param_key])
        return ret_val
