import matplotlib

class GcodeCommand:
    """
    Represents universal g-code command line
    """
    # Self notes for creating documentation:
    # initialization parameters: user_string
    # attributes: line_string, command, params
    # methods: get_command
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
