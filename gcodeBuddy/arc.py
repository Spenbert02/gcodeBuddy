import sys

class arc:
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
                if 0 <= kwargs["start_angle"] <= 360:
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
                if 0 <= kwargs["end_angle"] <= 360:
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
            if 0 <= new_start_angle <= 360:
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
            if 0 <= new_end_angle <= 360:
                self.start_angle = new_end_angle
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
