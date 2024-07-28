"""
Code with functions for converting power values into Watt(w) for:
1 - Horse Power(hp)
2 - Kilowatt(kw)
3 - Metric Horse Power(ps or cv)
"""

def w_to_hp(w_input:float):
    """
    Function for converting the power value in Watt(w) to Horse Power(hp).

    Args:
        w_input (float): Input with power value in Watt(w)

    Returns:
        float: Power value converted into Horse Power(hp).
    """

    result = w_input * 0.0013410221
    return result

def w_to_kw(w_input:float):
    """
    Function for converting the power value in Watt(w) to Kilowatt(kw).

    Args:
        w_input (float): Input with power value in Watt(w)

    Returns:
        float: Power value converted into Kilowatt(kw).
    """

    result = w_input * 0.001
    return result

def w_to_mhp(w_input:float):
    """
    Function for converting the power value in Watt(w) to Metric Horse Power(ps or cv).

    Args:
        w_input (float): Input with power value in Watt(w)

    Returns:
        float: Power value converted into Metric Horse Power(ps or cv).
    """

    result = w_input * 0.0013596216
    return result
