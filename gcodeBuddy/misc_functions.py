def unit_convert(value, current_units, needed_units):
    """
    Returns float, converted from given units into desired units
    """
    if not isinstance(value,(int, float)):
        return None

    if not isinstance(current_units, str):
        return None

    if not isinstance(needed_units, str):
        return None

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

    for i in range(3):  # iterating through categories
        if current_units in units[i] and needed_units in units[i]:  # if both units in same category
            return value * ((unit_vals[i][units[i].index(needed_units)]) / (unit_vals[i][units[i].index(current_units)]))  # perform calculation
    return None  # line will be reached if both units aren't in same category
