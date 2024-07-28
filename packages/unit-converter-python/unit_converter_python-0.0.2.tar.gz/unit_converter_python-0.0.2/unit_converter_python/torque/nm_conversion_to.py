"""
Code with functions for converting torque values into Newton Meter(Nm) for:
1 - Kilogram-force Meter (kgf·m)
2 - Pound-Force Foot (lbf·ft)
3 - Pound-Force Inch (lbf·in)
"""

def nm_to_kgfm(nm_input: float):
    """
    Function for converting the torque value in Newton Meter(Nm) to Kilogram-force Meter (kgf·m).

    Args:
        nm_input (float): Input with torque value in Newton Meter(Nm).

    Returns:
        float: Torque value converted into Kilogram-force Meter (kgf·m).
    """

    result = nm_input * 0.1019716213
    return result

def nm_to_lbfft(nm_input: float):
    """
    Function for converting the torque value in Newton Meter to Pound-Force Foot(lbf.ft).

    Args:
        nm_input (float): Input with torque value in Newton Meter(Nm).

    Returns:
        float: Torque value converted into Pound-Force Foot(lbf.ft).
    """

    result = nm_input * 0.7375621493
    return result

def nm_to_lbfin(nm_input: float):
    """
    Function for converting the torque value in Newton Meter to Pound-Force Inch(lbf.in).

    Args:
        nm_input (float): Input with torque value in Newton Meter(Nm).

    Returns:
        float: Torque value converted into Pound-Force Inch(lbf.in).
    """

    result = nm_input * 8.8507457916
    return result
