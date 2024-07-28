"""
Code with functions for converting power values into Metric Horse Power(ps or cv) for:
1 - Horse Power(hp)
2 - Kilowatt(kw)
3 - Watt(w)
"""

def mhp_to_hp(mhp_input:float):
    """
    Function for converting the power value in Metric Horse Power(ps or cv) to Horse Power(hp).

    Args:
        mhp_input (float): Input with power value in Metric Horse Power(ps or cv).

    Returns:
        float: Power value converted into Horse Power(hp).
    """

    result = mhp_input * 0.9863200706
    return result

def mhp_to_kw(mhp_input:float):
    """
    Function for converting the power value in Metric Horse Power(ps or cv) to Kilowatt(kw).

    Args:
        mhp_input (float): Input with power value in Metric Horse Power(ps or cv).

    Returns:
        float: Power value converted into Kilowatt(kw).
    """

    result = mhp_input * 0.73549875
    return result

def mhp_to_w(mhp_input:float):
    """
    Function for converting the power value in Metric Horse Power(ps or cv) to Watt(w).

    Args:
        mhp_input (float): Input with power value in Metric Horse Power(ps or cv).

    Returns:
        float: Power value converted into Watt(w).
    """

    result = mhp_input * 735.49875
    return result
