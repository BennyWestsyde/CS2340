def dec_int2bin_int(dec_int:str) -> str:
    """ Convert a decimal integer to a binary integer

    Args:
        dec_int (str): A decimal integer in string format

    Returns:
        str: A binary integer in string format
    """
    try:
        return str(bin(int(dec_int))[2:])
    except ValueError:
        return "Alert: The input is not a decimal integer."


def bin_int2dec_int(bin_int:str) -> str:
    """ Convert a binary integer to a decimal integer

    Args:
        bin_int (str): A binary integer in string format

    Returns:
        str: A decimal integer in string format
    """
    try:
        return str(int(bin_int, 2))
    except ValueError:
        return "Alert: The input is not a binary integer."
