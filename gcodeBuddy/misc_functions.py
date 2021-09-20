# for dev: error checked

import sys

def unit_convert(value, current_units, needed_units):
    """
    Returns float, converted from given units into desired units
    """

    err_msg = "Error in gcodeBuddy.unit_convert(): "

    if not isinstance(value, (int, float)):
        print(err_msg + "Argument 'value' of non-int/non-float type")
        sys.exit(1)

    if not isinstance(current_units, str):
        print(err_msg + "Argument 'current_units' of non-string type")
        sys.exit(1)

    if not isinstance(needed_units, str):
        print(err_msg + "Argument 'needed_units' of non-string type")
        sys.exit(1)

    units = (
        ("mm", "cm", "m", "in", "ft"),  # distance
        ("mm/sec", "mm/min", "cm/sec", "cm/min", "m/sec", "m/min", "in/sec", "in/min", "ft/sec", "ft/min"),  # speed
        ()  # acceleration
    )

    unit_vals = (
        (1000.0, 100.0, 1.0, 39.37, 3.281),  # distance
        (1000.0, 60000.0, 100.0, 6000.0, 1.0, 60.0, 39.37, 2362.0, 3.280, 196.9),  # speed
        ()  # acceleration
    )

    current_units = current_units.lower()
    needed_units = needed_units.lower()

    for i in range(3):  # iterating through categories
        if current_units in units[i] and needed_units in units[i]:  # if both units in same category
            return value * ((unit_vals[i][units[i].index(needed_units)]) / (unit_vals[i][units[i].index(current_units)]))  # perform calculation
    # point will be reached if units aren't in same category
    print(err_msg + "Unrecognized units passed in argument 'current_units' or 'needed_units'")
