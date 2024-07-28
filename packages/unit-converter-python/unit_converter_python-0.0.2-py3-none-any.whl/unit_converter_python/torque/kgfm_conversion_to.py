"""
Code with functions for converting torque values into Kilogram-force Meter (kgf·m) for:
1 - Newton Meter(Nm)
2 - Pound-Force Foot (lbf·ft)
3 - Pound-Force Inch (lbf·in)
"""

def kgfm_to_nm(kgfm_input: float):
    """
    Function for converting the torque value in Kilogram-force Meter (kgf·m) to Newton Meter(Nm).

    Args:
        kgfm_input (float): Input with torque value in Kilogram-force Meter (kgf·m).

    Returns:
        float: Torque value converted into Newton Meter(Nm).
    """

    result = kgfm_input * 9.8066500286
    return result

def kgfm_to_lbfft(kgfm_input: float):
    """
    Function for converting the torque value in Kilogram-force Meter (kgf·m) to 
    Pound-Force Foot (lbf·ft).

    Args:
        kgfm_input (float): Input with torque value in Kilogram-force Meter (kgf·m).

    Returns:
        float: Torque value converted into Pound-Force Foot (lbf·ft).
    """

    result = kgfm_input * 7.2330138723
    return result

def kgfm_to_lbfin(kgfm_input: float):
    """
    Function for converting the torque value in Kilogram-force Meter (kgf·m) to 
    Pound-Force Inch (lbf·in).

    Args:
        kgfm_input (float): Input with torque value in Kilogram-force Meter (kgf·m).

    Returns:
        float: Torque value converted into Pound-Force Inch (lbf·in).
    """

    result = kgfm_input * 86.796207741
    return result
