"""
Code with functions for converting power values into Kilowatt(kw) for:
1 - Horse Power(hp)
2 - Metric Horse Power(ps or cv)
3 - Watt(w)
"""

def kw_to_hp(kw_input:float):
    """
    Function for converting the power value in Kilowatt(kw) to Horse Power(hp).

    Args:
        kw_input (float): Input with power value in Kilowatt(kw).

    Returns:
        float: Power value converted into Horse Power(hp).
    """

    result = kw_input * 1.3410220896
    return result

def kw_to_ps(kw_input:float):
    """
    Function for converting the power value in Kilowatt(kw) to Metric Horse Power(ps or cv).

    Args:
        kw_input (float): Input with power value in Kilowatt(kw).

    Returns:
        float: Power value converted into Metric Horse Power(ps or cv).
    """

    result = kw_input * 1.3596216173
    return result

def kw_to_w(kw_input:float):
    """
    Function for converting the power value in Kilowatt(kw) to Watt(w).

    Args:
        kw_input (float): Input with power value in Kilowatt(kw).

    Returns:
        float: Power value converted into Watt(w).
    """

    result = kw_input * 1000
    return result
