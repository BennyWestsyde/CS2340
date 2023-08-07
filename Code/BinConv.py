from Dbl2Bin import dec_float2double_bin_float, double_bin_float2dec_float
from Half2Bin import dec_float2half_bin_float, half_bin_float2dec_float
from Int2Bin import dec_int2bin_int, bin_int2dec_int
from Sngl2Bin import dec_float2single_bin_float, single_bin_float2dec_float

def main(debug:bool=False):
    while True:
        print("1. Dec Int 2 Bin Int")
        print("2. Bin Int 2 Dec Int")
        print("3. Dec Flt 2 Half-Prec Bin Flt")
        print("4. Dec Flt 2 Single-Prec Bin Flt")
        print("5. Dec Flt 2 Double-Prec Bin Flt")
        print("6. Half-Prec Bin Flt 2 Dec Flt")
        print("7. Single-Prec Bin Flt 2 Dec Flt")
        print("8. Double-Prec Bin Flt 2 Dec Flt")
        print("9. Exit")
        choice = input("Enter choice: ")
        if choice == '9':
            break
        num = input("Enter number to convert: ")
        if choice == '1':
            bin_int = dec_int2bin_int(num)
            print(bin_int)
        elif choice == '2':
            dec_int = bin_int2dec_int(num)
            print(dec_int)
        elif choice == '3':
            half_bin_float = dec_float2half_bin_float(num, debug=debug)
            print("Sign bit: |" + half_bin_float[0] + "        |")
            print("Exponent: |" + half_bin_float[1:5], half_bin_float[5:6] + "   |")
            print("Mantissa: |" + half_bin_float[6:10], half_bin_float[10:14] + "|")
            print("          |" + half_bin_float[14:16], "      |")
            print("Full binary float: \n" + half_bin_float)
        elif choice == '4':
            single_bin_float = dec_float2single_bin_float(num, debug=debug)
            print("Sign bit: |" + single_bin_float[0] + "        |")
            print("Exponent: |" + single_bin_float[1:5], single_bin_float[5:9] + "|")
            # print the mantissa, 4 bits at a time
            print("Mantissa: |" + single_bin_float[9:13], single_bin_float[13:17] + "|")
            print("          |" + single_bin_float[17:21], single_bin_float[21:25] + "|")
            print("          |" + single_bin_float[25:29], single_bin_float[29:32] + " |")
            print("Full binary float: \n" + single_bin_float)

        elif choice == '5':
            double_bin_float = dec_float2double_bin_float(num, debug=debug)
            print("Sign bit: |" + double_bin_float[0] + "        |")
            print("Exponent: |" + double_bin_float[1:5], double_bin_float[5:9] + "|")
            print("          |" + double_bin_float[9:12] + "      |")
            # print the mantissa, 4 bits at a time
            print("Mantissa: |" + double_bin_float[12:16], double_bin_float[16:20] + "|")
            print("          |" + double_bin_float[20:24], double_bin_float[24:28] + "|")
            print("          |" + double_bin_float[28:32], double_bin_float[32:36] + "|")
            print("          |" + double_bin_float[36:40], double_bin_float[40:44] + "|")
            print("          |" + double_bin_float[44:48], double_bin_float[48:52] + "|")
            print("          |" + double_bin_float[52:56], double_bin_float[56:60] + "|")
            print("          |" + double_bin_float[60:64], "    |")
            print("Full binary float: \n" + double_bin_float)
        elif choice == '6':
            print(half_bin_float2dec_float(num))
        elif choice == '7':
            print(single_bin_float2dec_float(num))
        elif choice == '8':
            print(double_bin_float2dec_float(num))
        else:
            print("Invalid choice")
        input("Press Enter to continue...")

main(debug=True)