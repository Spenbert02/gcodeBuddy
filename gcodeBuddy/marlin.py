# for dev: error checked

import sys

import numpy as np

from gcodeBuddy import marlin_commands, angle, Arc, centers_from_params


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
        if command_list[0] in marlin_commands():
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


def command_to_arc(curr_pos, command):
    """
    Function to return an Arc object given a Command object and a starting position
    """

    err_msg = "Error in marlin.command_to_arc(): "

    # error checking curr_pos
    if isinstance(curr_pos, (list, tuple)):
        if len(curr_pos) == 2:
            valid_types = True
            for coord in curr_pos:
                if not isinstance(coord, (int, float)):
                    valid_types = False
            if not valid_types:
                print(err_msg + "Element in argument 'curr_pos' of non-int/non-float type")
                sys.exit(1)
        else:
            print(err_msg + "Argument 'curr_pos' does not contain two elements")
            sys.exit(1)
    else:
        print(err_msg + "Argument 'curr_pos' of non-list/non-tuple type")
        sys.exit(1)

    # error checking command - error checking done in Command.__init__(), just need to make sure command is passed
    if not isinstance(command, Command):
        print(err_msg + "Argument 'command' of non-Command type")
        sys.exit(1)
    if command.get_command() not in ("G2", "G3"):
        print(err_msg + "Command must be 'G2' or 'G3' for arc conversion")
        sys.exit(1)

    # organizing parameters into list (for error checking)
    param_list =[]
    for letter in "XYIJR":
        if command.has_param(letter):
            param_list.append(letter)

    # setting direction
    direction = "c"
    if command.get_command() == "G3":
        direction = "cc"

    if ("I" in param_list) or ("J" in param_list):  # I and J parameters
        # more error checking
        if "R" in param_list:
            print(err_msg + "Command cannot mix parameter 'R' with parameters 'I' and 'J' for arc conversion")
            sys.exit(1)
        # if only given I, J, or I and J
        if ("X" not in param_list) and ("Y" not in param_list):
            if param_list == ["I"]:  # I
                I = command.get_param("I")
                center = [curr_pos[0] + I, curr_pos[1]]
                radius = I
                start_angle = angle(center, curr_pos)
                end_angle = angle(center, curr_pos)
                return Arc(center=center,
                           radius=radius,
                           start_angle=start_angle,
                           end_angle=end_angle,
                           direction=direction)
            elif param_list == ["J"]:  # J
                J = command.get_param("J")
                center = [curr_pos[0], curr_pos[1] + J]
                radius = J
                start_angle = angle(center, curr_pos)
                end_angle = angle(center, curr_pos)
                return Arc(center=center,
                           radius=radius,
                           start_angle=start_angle,
                           end_angle=end_angle,
                           direction=direction)
            else:  # I J
                I = command.get_param("I")
                J = command.get_param("J")
                center = [curr_pos[0] + I, curr_pos[1] + J]
                radius = np.sqrt(I**2 + J**2)
                start_angle = angle(center, curr_pos)
                end_angle = angle(center, curr_pos)
                return Arc(center=center,
                           radius=radius,
                           start_angle=start_angle,
                           end_angle=end_angle,
                           direction=direction)
        # if given X and I or Y and J (require more intricate handling)
        if param_list == ["X", "I"]:
            X = command.get_param("X")
            I = command.get_param("I")
            if curr_pos[0] + (2 * I) - X < 0.001:
                center = [curr_pos[0] + I, curr_pos[1]]
                radius = abs(I)
                start_angle = angle(center, curr_pos)
                end_angle = angle(center, [X, curr_pos[1]])
                return Arc(center=center,
                           radius=radius,
                           start_angle=start_angle,
                           end_angle=end_angle,
                           direction=direction)
            else:
                print(err_msg + "Invalid Command parameters for arc conversion (cannot create arc from given X and I values)")
                sys.exit(1)
        elif param_list == ["Y", "J"]:
            Y = command.get_param("Y")
            J = command.get_param("J")
            if curr_pos[1] + (2 * J) - Y < 0.001:
                center = [curr_pos[0], curr_pos[1] + J]
                radius = abs(J)
                start_angle = angle(center, curr_pos)
                end_angle = angle(center, [curr_pos[0], Y])
                return Arc(center=center,
                           radius=radius,
                           start_angle=start_angle,
                           end_angle=end_angle,
                           direction=direction)
            else:
                print(err_msg + "Invalid Command parameters for arc conversion (cannot create arc from given Y and J values)")
                sys.exit(1)
        # must have X or Y, I or J
        # setting I parameter
        I = 0
        if "I" in param_list:
            I = command.get_param("I")
        # setting J parameter
        J = 0
        if "J" in param_list:
            J = command.get_param("J")
        # setting X parameter
        X = curr_pos[0]
        if "X" in param_list:
            X = command.get_param("X")
        # setting Y parameter
        Y = curr_pos[1]
        if "Y" in param_list:
            Y = command.get_param("Y")
        # returning arc object
        center = [curr_pos[0] + I, curr_pos[1] + J]
        radius = np.sqrt(I**2 + J**2)
        start_angle = angle(center, curr_pos)
        end_angle = angle(center, [X, Y])
        return Arc(center=center,
                   radius=radius,
                   start_angle=start_angle,
                   end_angle=end_angle,
                   direction=direction)
    elif "R" in param_list:  # R parameter
        if "X" in param_list or "Y" in param_list:
            # setting X parameter
            X = curr_pos[0]
            if "X" in param_list:
                X = command.get_param("X")
            # setting Y parameter
            Y = curr_pos[1]
            if "Y" in param_list:
                Y = command.get_param("Y")
            # setting R parameter
            R = command.get_param("R")
            need_smaller = R > 0  # if smaller angle arc necessary
            R = np.abs(R)
            # creating test arc, if is smaller than 180 deg then return, otherwise choose other center and create and return that arc
            if (np.abs(np.sqrt((X - curr_pos[0])**2 + (Y - curr_pos[1])**2)) / 2) > R:  # distance between points greater than radius
                R = (np.abs(np.sqrt((X - curr_pos[0])**2 + (Y - curr_pos[1])**2)) / 2)
            centers = centers_from_params(curr_pos, (X, Y), R)
            # creating test arc
            test_arc = Arc(center=centers[0],
                           radius=R,
                           start_angle=angle(centers[0], curr_pos),
                           end_angle=angle(centers[0], (X, Y)),
                           direction=direction)
            if need_smaller:
                if test_arc.get_angle() <= 180:
                    return test_arc
                else:
                    return Arc(center=centers[1],
                               radius=R,
                               start_angle=angle(centers[1], curr_pos),
                               end_angle=angle(centers[1], (X, Y)),
                               direction=direction)
            else:
                if test_arc.get_angle() <= 180:
                    return Arc(center=centers[1],
                               radius=R,
                               start_angle=angle(centers[1], curr_pos),
                               end_angle=angle(centers[1], (X, Y)),
                               direction=direction)
                else:
                    return test_arc
        else:
            print(err_msg + "Invalid Command parameters for arc conversion (X or Y required with R)")
            sys.exit(1)
    else:  # no required parameters
        print(err_msg + "Invalid Command parameters for arc conversion (I, J, or R is required)")
        sys.exit(1)


# debug station
if __name__ == "__main__":
    while True:
        test_command_str = input("command: ")
        test_command = Command(test_command_str)
        test_arc = command_to_arc([100, 100], test_command)
        test_arc.plot()
        print()

