"""
Code with functions for converting torque values into Pound-Force Inch (lbf·in) for:
1 - Kilogram-force Meter (kgf·m)
2 - Newton Meter(Nm)
3 - Pound-Force Inch (lbf·in)
"""

def lbfft_to_kgfm(lbfft_input:float):
    """
    Function for converting the torque value in Pound-Force Foot (lbf·ft) to 
    Kilogram-force Meter (kgf·m).

    Args:
        lbfft_input (float): Input with torque value in Pound-Force Foot (lbf·ft).

    Returns:
        float: Torque value converted into Kilogram-force Meter (kgf·m).
    """

    result = lbfft_input * 0.138254954
    return result

def lbfft_to_nm(lbfft_input:float):
    """
    Function for converting the torque value in Pound-Force Foot (lbf·ft) to Newton Meter(Nm).

    Args:
        lbfft_input (float): Input with torque value in Pound-Force Foot (lbf·ft).

    Returns:
        float: Torque value converted into Newton Meter(Nm).
    """

    result = lbfft_input * 1.3558179483
    return result

def lbfft_to_lbfin(lbfft_input:float):
    """
    Function for converting the torque value in Pound-Force Foot (lbf·ft) to 
    Pound-Force Inch (lbf·in).

    Args:
        lbfft_input (float): Input with torque value in Pound-Force Foot (lbf·ft).

    Returns:
        float: Torque value converted into Pound-Force Inch (lbf·in).
    """

    result = lbfft_input * 12.000005706
    return result
