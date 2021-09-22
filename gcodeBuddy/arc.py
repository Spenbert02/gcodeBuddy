# for dev: error checked

import sys
from matplotlib import pyplot as plt
import numpy as np


class Arc:
    """
    Represents an arc toolpath
    """
    # for documentation notes:
    # attributes: center, radius, start_angle, end_angle, direction
    # methods: get_xxx(), set_xxx()
    def __init__(self, **kwargs):
        """
        Initialization method
        """
        err_msg = "Error in arc.__init__(): "
        # ensuring valid keyword arguments passed
        req_args = ("center", "radius", "start_angle", "end_angle", "direction")
        for keyword in kwargs:
            if keyword not in req_args:
                print(err_msg + "unrecognized keyword argument '" + keyword + "'")
                sys.exit(1)

        # ensuring valid center argument
        if "center" in kwargs:
            if isinstance(kwargs["center"], list):
                if len(kwargs["center"]) == 2:
                    valid_coord_types = True
                    for coord in kwargs["center"]:
                        if not isinstance(coord, (int, float)):
                            valid_coord_types = False
                    if valid_coord_types:
                        self.center = kwargs["center"]
                    else:
                        print(err_msg + "entry in keyword argument 'center' of non-int, non-float type")
                        sys.exit(1)
                else:
                    print(err_msg + "keyword argument 'center' not of length 2")
                    sys.exit(1)
            else:
                print(err_msg + "keyword argument 'center' of non-list type")
                sys.exit(1)
        else:
            print(err_msg + "required keyword argument 'center' not passed")
            sys.exit(1)

        # ensuring valid radius argument
        if "radius" in kwargs:
            if isinstance(kwargs["radius"], (int, float)):
                self.radius = kwargs["radius"]
            else:
                print(err_msg + "keyword argument 'radius' of non-int, non-float type")
                sys.exit(1)
        else:
            print(err_msg + "required keyword argument 'radius' not passed")
            sys.exit(1)

        # ensuring valid start_angle argument
        if "start_angle" in kwargs:
            if isinstance(kwargs["start_angle"], (int, float)):
                if 0 <= kwargs["start_angle"] < 360:
                    self.start_angle = kwargs["start_angle"]
                else:
                    print(err_msg + "keyword argument 'start_angle' pass value out of range [0, 360]")
                    sys.exit(1)
            else:
                print(err_msg + "keyword argument 'start_angle' of non-int, non-float type")
                sys.exit(1)
        else:
            print(err_msg + "required keyword argument 'start_angle' not passed")
            sys.exit(1)

        # ensuring valid end_angle argument
        if "end_angle" in kwargs:
            if isinstance(kwargs["end_angle"], (int, float)):
                if 0 <= kwargs["end_angle"] < 360:
                    self.end_angle = kwargs["end_angle"]
                else:
                    print(err_msg + "keyword argument 'end_angle' pass value out of range [0, 360]")
                    sys.exit(1)
            else:
                print(err_msg + "keyword argument 'end_angle' of non-int, non-float type")
                sys.exit(1)
        else:
            print(err_msg + "required keyword argument 'end_angle' not passed")
            sys.exit(1)

        # ensuring valid direction argument
        if "direction" in kwargs:
            if kwargs["direction"] in ("c", "cc"):
                self.direction = kwargs["direction"]
            else:
                print(err_msg + "keyword argument 'direction' must be string \"c\" (clockwise) or \"cc\" (counter-clockwise)")
                sys.exit(1)
        else:
            print(err_msg + "keyword argument 'direction' not passed")
            sys.exit(1)

    def get_center(self):
        """
        Returns center as 2 element list of ints/floats
        """
        return self.center

    def get_radius(self):
        """
        Returns radius as int/float
        """
        return self.radius

    def get_start_angle(self):
        """
        Returns start_angle as int/float
        """
        return self.start_angle

    def get_end_angle(self):
        """
        Returns end_angle as int/float
        """
        return self.end_angle

    def get_direction(self):
        """
        Returns direction as string (either "c" or "cc")
        """
        return self.direction

    def get_angle(self):
        """
        Returns angle that arc carves out in degrees as float
        """
        if np.abs(self.start_angle - self.end_angle) < 0.001:  # approximate equality, given inaccuracy of floats
            return 360
        elif self.start_angle > self.end_angle:
            if self.direction == "cc":
                return 360 - (self.start_angle - self.end_angle)
            else:
                return self.start_angle - self.end_angle
        else:
            if self.direction == "cc":
                return self.end_angle - self.start_angle
            else:
                return 360 - (self.end_angle - self.start_angle)

    def set_center(self, new_center):
        """
        Sets center attribute to new_center
        """
        err_msg = "Error in arc.set_center(): "
        # ensuring valid new_center argument
        if isinstance(new_center, list):
            if len(new_center) == 2:
                valid_coord_types = True
                for coord in new_center:
                    if not isinstance(coord, (int, float)):
                        valid_coord_types = False
                if valid_coord_types:
                    self.center = new_center
                else:
                    print(err_msg + "entry in argument 'new_center' of non-int, non-float type")
                    sys.exit(1)
            else:
                print(err_msg + "argument 'new_center' not of length 2")
                sys.exit(1)
        else:
            print(err_msg + "argument 'new_center' of non-list type")
            sys.exit(1)

    def set_radius(self, new_radius):
        """
        Sets radius attribute to new_radius
        """
        err_msg = "Error in arc.set_radius(): "
        # ensuring valid new_radius argument
        if isinstance(new_radius, (int, float)):
            self.radius = new_radius
        else:
            print(err_msg + "argument 'new_radius' of non-int, non-float type")
            sys.exit(1)

    def set_start_angle(self, new_start_angle):
        """
        Sets start_angle attribute to new_start_angle
        """
        err_msg = "Error in arc.set_start_angle(): "
        # ensuring valid new_start_angle argument
        if isinstance(new_start_angle, (int, float)):
            if 0 <= new_start_angle < 360:
                self.start_angle = new_start_angle
            else:
                print(err_msg + "argument 'new_start_angle' pass value out of range [0, 360]")
                sys.exit(1)
        else:
            print(err_msg + "argument 'new_start_angle' of non-int, non-float type")
            sys.exit(1)

    def set_end_angle(self, new_end_angle):
        """
        Sets end_angle attribute to new_end_angle
        """
        err_msg = "Error in arc.set_end_angle(): "
        # ensuring valid new_end_angle argument
        if isinstance(new_end_angle, (int, float)):
            if 0 <= new_end_angle < 360:
                self.end_angle = new_end_angle
            else:
                print(err_msg + "argument 'new_end_angle' pass value out of range [0, 360]")
                sys.exit(1)
        else:
            print(err_msg + "argument 'new_end_angle' of non-int, non-float type")
            sys.exit(1)

    def set_direction(self, new_direction):
        """
        Sets direction attribute to new_direction
        """
        err_msg = "Error in arc.set_direction(): "
        # ensuring valid new_direction argument
        if new_direction in ("c", "cc"):
            self.direction = new_direction
        else:
            print(err_msg + "argument 'new_direction' must be string \"c\" (clockwise) or \"cc\" (counter-clockwise)")
            sys.exit(1)

    def plot(self):
        # setting offsets based on center
        x_offset = self.center[0]
        y_offset = self.center[1]
        # determining start/end angles for arc plotting
        if np.abs(self.start_angle - self.end_angle) < 0.001:  # approximate equality, given inaccuracy of floats
            if self.direction == "cc":
                theta_1 = self.start_angle * (np.pi / 180)
                theta_2 = (self.end_angle + 360) * (np.pi / 180)
            else:
                theta_1 = (self.start_angle + 360) * (np.pi / 180)
                theta_2 = self.end_angle * (np.pi / 180)
        elif self.start_angle > self.end_angle and self.direction == "cc":
            theta_1 = self.start_angle * (np.pi / 180)
            theta_2 = (self.end_angle + 360) * (np.pi / 180)
        elif self.start_angle < self.end_angle and self.direction == "c":
            theta_1 = (self.start_angle + 360) * (np.pi / 180)
            theta_2 = self.end_angle * (np.pi / 180)
        else:
            theta_1 = self.start_angle * (np.pi / 180)
            theta_2 = self.end_angle * (np.pi / 180)
        # defining points to plot:
        t_vals = np.linspace(theta_1, theta_2, num=360)
        path_points = ((self.radius * np.cos(t_vals)) + x_offset, (self.radius * np.sin(t_vals)) + y_offset)
        start_point = ((self.radius * np.cos(theta_1)) + x_offset, (self.radius * np.sin(theta_1)) + y_offset)
        end_point = ((self.radius * np.cos(theta_2)) + x_offset, (self.radius * np.sin(theta_2)) + y_offset)
        # setting aspect ratio
        ax = plt.gca()
        ax.set_aspect(1)
        # plotting and showing
        plt.plot(path_points[0], path_points[1], "b", label="path")
        plt.plot(start_point[0], start_point[1], "ro", label="start", alpha = 0.5)
        plt.plot(end_point[0], end_point[1], "go", label="end", alpha=0.5)
        plt.legend()
        plt.show()


# debug station
if __name__ == "__main__":
    test_arcs = []
    decide_char = "y"
    while decide_char == "y":
        center_x = float(input("x center: "))
        center_y = float(input("y center: "))
        radius = float(input("radius: "))
        start_angle = float(input("start_angle: "))
        end_angle = float(input("end_angle: "))
        direction = input("direction: ")
        arc = Arc(center=[center_x, center_y],
            radius=radius,
            start_angle=start_angle,
            end_angle=end_angle,
            direction=direction)
        print("angle: ", arc.get_angle())
        arc.plot()
        decide_char = input("Again? (y/n): ")
        print("\n")