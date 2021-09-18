import matplotlib

"""
gcode_command object for ***MARLIN*** g-code flavor
"""

class gcode_command:
    """
    Represents universal g-code command line
    """
    # Self notes for creating documentation:
    # initialization parameters: user_string
    # attributes: line_string, command, params
    # methods: get_command, has_param, get_param, get_string
    def __init__(self, user_string):
        """
        Initialization method
        """
        self.line_string = user_string
        line_list = self.line_string.split(" ")
        self.command = line_list[0]
        self.params = []
        for i in range(97, 123):
            has_param = False
            for j in range(1, len(line_list)):
                if line_list[j][0].lower() == chr(i):
                    self.params.append(float(line_list[j][1:]))
                    has_param = True
                    break
            if not has_param:
                self.params.append(None)

    def get_command(self):
        """
        Returns Line instance's command as string
        """
        return self.command

    def has_param(self, param_char):
        """
        Returns True if line has given parameter, else returns False
        """
        param_char = param_char.lower()
        return self.params[ord(param_char) - 97] is not None

    def get_param(self, param_char):
        """
        Returns parameter value as float
        """
        param_char = param_char.lower()
        return self.params[ord(param_char) - 97]

    def set_param(self, param_char, param_val):
        """
        Sets given parameter character to given parameter value
        """
        param_char = param_char.lower()
        self.params[ord(param_char) - 97] = param_val

    def get_string(self):
        """
        Returns entire command line as string
        """
        ret_val = ""
        ret_val += self.command
        for i in range(26):
            if self.params[i] is not None:
                ret_val += " " + chr(i + 97).upper() + str(round(self.params[i], 2))
        return ret_val