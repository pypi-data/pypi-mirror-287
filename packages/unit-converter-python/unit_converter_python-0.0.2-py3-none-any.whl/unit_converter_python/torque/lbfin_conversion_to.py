"""
Code with functions for converting torque values into Pound-Force Inch (lbf·in) for:
1 - Kilogram-force Meter (kgf·m)
2 - Newton Meter(Nm)
3 - Pound-Force Foot (lbf·ft)
"""

def lbfin_to_kgfm(lbfin_input:float):
    """
    Function for converting the torque value in Pound-Force Inch (lbf·in) to 
    Kilogram-force Meter (kgf·m).

    Args:
        lbfin_input (float): Input with torque value in Pound-Force Inch (lbf·in).

    Returns:
        float: Torque value converted into Kilogram-force Meter (kgf·m).
    """

    result = lbfin_input * 0.0115212407
    return result

def lbfin_to_nm(lbfin_input:float):
    """
    Function for converting the torque value in Pound-Force Inch (lbf·in) to Newton Meter(Nm).

    Args:
        lbfin_input (float): Input with torque value in Pound-Force Inch (lbf·in).

    Returns:
        float: Torque value converted into Newton Meter(Nm).
    """

    result = lbfin_input * 0.1129847753
    return result

def lbfin_to_lbfft(lbfin_input:float):
    """
    Function for converting the torque value in Pound-Force Inch (lbf·in) to 
    Pound-Force Foot (lbf·ft).

    Args:
        lbfin_input (float): Input with torque value in Pound-Force Inch (lbf·in).

    Returns:
        float: Torque value converted into Pound-Force Foot (lbf·ft).
    """

    result = lbfin_input * 0.0833332937
    return result
