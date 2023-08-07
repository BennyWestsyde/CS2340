def bin_int_add(bin1, bin2, return_carry=False, debug=False):
    bin1 = bin1.zfill(16)
    bin2 = bin2.zfill(16)
    sum_bin = ''
    carry = 0
    for i in range(15, -1, -1):
        bit1 = int(bin1[i])
        bit2 = int(bin2[i])
        sum_bit = bit1 + bit2 + carry
        carry = sum_bit // 2
        sum_bin = str(sum_bit % 2) + sum_bin

    if return_carry:
        return sum_bin, carry
    if debug:
        print(f"Adding bits: {bit1} and {bit2}, Result: {sum_bin}, Carry: {carry}")

    return sum_bin

def bin_int_sub(bin1, bin2, debug=False):
    # Ensure bin1 and bin2 are the same length
    max_len = max(len(bin1), len(bin2))
    bin1 = bin1.zfill(max_len)
    bin2 = bin2.zfill(max_len)

    # If bin2 > bin1, swap bin1 and bin2
    if bin1 < bin2:
        bin1, bin2 = bin2, bin1

    result = ''
    carry = '0'

    # Subtract bits from right to left
    for i in range(max_len - 1, -1, -1):
        bit1 = int(bin1[i])
        bit2 = int(bin2[i])

        # Subtract bits and carry
        if carry == '1':
            if bit1 == bit2:
                result = '1' + result
                carry = str(bit2)
            else:
                result = '0' + result
                carry = str(bit1)
        else:
            if bit1 == bit2:
                result = '0' + result
                carry = str(bit1)
            else:
                result = '1' + result
                carry = str(bit2)

        if debug:
            print(f"Subtracting bits: {bit1} and {bit2}, Result: {result}, Carry: {carry}")

    return result


def bin_int_mul(bin1, bin2, debug=False):
    bin1 = bin1[::-1]
    bin2 = bin2[::-1]

    result = '0'

    for i in range(len(bin1)):
        for j in range(len(bin2)):
            if bin1[i] == '1' and bin2[j] == '1':
                temp_result = '1' + '0' * (i + j)
                result = bin_int_add(result, temp_result)

                if debug:
                    print(f"Multiplying bits at positions {i} and {j}, Temp Result: {temp_result}, Cumulative Result: {result}")

    return result


def bin_int_div(bin1, bin2, debug=False):
    if bin2 == '0':
        raise ValueError("Divisor cannot be 0")

    quotient = '0'
    remainder = bin1

    while bin_int_sub(remainder, bin2) != '0':
        remainder = bin_int_sub(remainder, bin2)
        quotient = bin_int_add(quotient, '1')

        if debug:
            print(f"Subtracting {bin2} from {remainder}, Quotient: {quotient}, Remainder: {remainder}")

    return quotient
