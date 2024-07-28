"""
Code with functions for converting power values into Horse Power(hp) for:
1 - Kilowatt(kw)
2 - Metric Horse Power(ps or cv)
3 - Watt(w)
"""

def hp_to_kw(hp_input:float):
    """
    Function for converting the power value in Horse Power(hp) to Kilowatt(kw).

    Args:
        hp_input (float): Input with power value in Horse Power(hp).

    Returns:
        float: Power value converted into Kilowatt(kw).
    """

    result = hp_input * 0.7456998716
    return result

def hp_to_ps(hp_input:float):
    """
    Function for converting the power value in Horse Power(hp) to Metric Horse Power(ps or cv).

    Args:
        hp_input (float): Input with power value in Horse Power(hp).

    Returns:
        float: Power value converted into Metric Horse Power(ps or cv).
    """

    result = hp_input * 1.0138696654
    return result

def hp_to_w(hp_input:float):
    """
    Function for converting the power value in Horse Power(hp) to Watt(w).

    Args:
        hp_input (float): Input with power value in Horse Power(hp).

    Returns:
        float: Power value converted into Watt(w).
    """

    result = hp_input * 745.69987158
    return result
