def dec_float2single_bin_float(dec_float:str, debug:bool=False) -> str:
    """ Convert a decimal float to a single-precision binary float according to IEEE 754 standard

    Args:
        dec_float (str): A decimal float in string format
        debug (bool): If true, print the intermediate steps in the conversion process

    Returns:
        str: A single-precision binary float in string format
    """
    # Constants for single precision
    sign_bit_mask = 0x80000000
    exponent_mask = 0x7F800000
    fraction_mask = 0x007FFFFF
    exponent_bias = 127
    min_exp = -126
    max_exp = 127
    max_value = 3.4028235e38
    min_value = 1.17549435e-38
    # Convert to float
    try:
        dec_float_test = float(dec_float)
    except ValueError:
        return "Alert: The input is not a decimal floating point number."
    # Check for overflow and underflow
    if dec_float_test > max_value:
        return "Alert: Overflow. The input number is larger than the largest possible number in single precision."
    elif dec_float_test != 0.0 and abs(dec_float_test) < min_value:
        return "Alert: Underflow. The input number is closer to zero than the smallest possible number in single precision."

    # Calculate sign bit
    sign_bit = 0 if dec_float_test >= 0 else 1
    dec_float_whole, dec_float_fraction = str(abs(dec_float_test)).split(".") # Split the decimal float into whole and fractional parts
    bin_float_whole = bin(int(dec_float_whole))[2:] # Convert the whole part to binary
    bin_float_fraction = "" # Initialize the fractional part in binary

    # Convert the fractional part to binary
    fraction = "0." + dec_float_fraction
    while float(fraction) > 0:
        if debug:
            print(str(fraction)[:6],"* 2", end=" = ")
        fraction = float(fraction) * 2
        if debug:
            print(str(fraction)[:6], end=" ")
        if float(fraction) >= 1:
            if debug:
                print("(1)", end=" ")
            bin_float_fraction += "1"
            fraction -= 1
        else:
            if debug:
                print("(0)", end=" ")
            bin_float_fraction += "0"
        if debug:
            input()

    # Handle the case when there's no non-zero number before the decimal point
    shifts = 0
    if bin_float_whole == "0":
        # Find the first '1' in the fraction
        index_of_first_one = bin_float_fraction.find('1')
        if index_of_first_one != -1:
            # Shift the point to after the first '1'
            shifts = index_of_first_one + 1
            bin_float_whole = '1'
            bin_float_fraction = bin_float_fraction[shifts:]

    # Calculate the exponent and bias it
    exponent = len(bin_float_whole) - 1 + exponent_bias - shifts
    bin_exponent = (lambda s, n, c: c * (n - len(s)) + s  if len(s) < n else s[:n])(bin(exponent)[2:], 8, "0") # 8 bits for single precision

    # Create the mantissa
    mantissa = bin_float_whole[1:] + bin_float_fraction
    mantissa = (lambda s, n, c: c * (n - len(s))+ s if len(s) < n else s[:n])(mantissa, 23, "0")    # 23 bits for single precision

    # Format the final result
    binary_float = str(sign_bit) + bin_exponent + mantissa
    return binary_float


def single_bin_float2dec_float(bin_float:str, debug:bool=False) -> str:
    """ Convert a single-precision binary float to a decimal float according to IEEE 754 standard

    Args:
        bin_float (str): A single-precision binary float in string format
        debug (bool): If true, print the intermediate steps in the conversion process

    Returns:
        str: A decimal float in string format
    """
    # Constants for single precision
    sign_bit_mask = 0x80000000
    exponent_mask = 0x7F800000
    fraction_mask = 0x007FFFFF
    exponent_bias = 127
    min_exp = -126
    max_exp = 127

    # Check the length of the binary float
    if len(bin_float) != 32:
        return "Alert: The input is not a 32-bit single-precision binary floating point number."

    # Extract the sign bit, exponent, and fraction from the binary float
    sign_bit = int(bin_float[0])
    exponent = int(bin_float[1:9], 2)
    fraction = "1" + bin_float[9:] # Add the leading 1 for the normalized mantissa

    # Convert the fraction to decimal
    dec_fraction = 0
    for i in range(24):
        dec_fraction += int(fraction[i]) * 2**-(i)

    # Calculate the decimal float
    dec_float = (-1)**sign_bit * dec_fraction * 2**(exponent - exponent_bias)
    return str(dec_float)
