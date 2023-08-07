# Binary Arithmetic
## Integer Addition

#### **_Summary:_**
Binary addition involves adding two binary numbers. Carrying over occurs when the sum of two bits is 2 or greater.

#### **_Definitions:_**
- **Bit**: A binary digit, either 0 or 1.
- **Carry**: The value carried to the next column when two bits sum to 2 or more.

#### **_Example:_**
Adding $1101 + 0011$:
$$
\begin{aligned}
1111\Lsh &\text{ Remainder}\\
 1101\ &\\
+0011\ &\\
\hline
 10000
\end{aligned}
$$

#### **_Tricky Things to Remember:_**
- Don't forget to carry over when the sum of two bits is 2 or greater.

***

## Integer Subtraction

#### **_Summary:_**
Binary subtraction involves borrowing from the next column when the subtrahend is greater than the minuend.

#### **_Definitions:_**
- **Borrow**: Taking value from the next column when the subtrahend is greater than the minuend.

#### **_Example:_**
Subtracting $1101 - 0011$:
$$
\begin{aligned}
 1101&\\
-0011&\\
\hline
 1010&
\end{aligned}
$$

#### **_Tricky Things to Remember:_**
- Don't forget to borrow from the next column when needed.

***

## Integer Division

#### **_Summary:_**
Binary division involves dividing the dividend by the divisor to find the quotient and remainder.

#### **_Definitions:_**
- **Dividend**: The number to be divided.
- **Divisor**: The number by which division is to be performed.
- **Quotient**: The result of the division.
- **Remainder**: The remaining part after division.

#### **_Example:_**
Dividing $1101 \div 11$:
$$
\begin{aligned}
    \phantom{)1}100& R 1\\
 11\overline{)1101}&\\
 \underline{1100}& \\
 0001\\
\end{aligned}
$$
Quotient: \(100\), Remainder: \(10\)

#### **_Tricky Things to Remember:_**
- Carefully follow the division steps to obtain the correct quotient and remainder.

***

## Integer Multiplication

#### **_Summary:_**
Binary multiplication involves adding partial products obtained by multiplying the multiplicand by each bit of the multiplier.

#### **_Definitions:_**
- **Multiplicand**: The number to be multiplied.
- **Multiplier**: The number by which multiplication is to be performed.

#### **_Example:_**
Multiplying $1101 \times 0011$:
$$
\begin{aligned}
 1101&\\
\times0011&\\
\hline
 1101&\\
+1101\ \ &\\
\hline
 100111&
\end{aligned}
$$

#### **_Tricky Things to Remember:_**
- Ensure correct alignment of partial products to obtain the correct result.

***

## Floating Point Addition

#### **_Summary:_**
Floating-point addition in binary involves aligning the exponents, adding the mantissas, and normalizing the result.

#### **_Definitions:_**
- **Sign Bit**: Indicates the sign of the number.
- **Exponent**: Represents the power of 2.
- **Mantissa**: The fractional part of the number.

#### **_Example:_**
Certainly! Here are the examples for floating-point arithmetic using half-precision, single-precision, and double-precision formats according to the IEEE 754 standard.

##### **_Half-Precision Example:_**
1. Convert both numbers to their IEEE 754 format.
2. Align the exponents by shifting the mantissa of the number with the smaller exponent.
3. Add mantissas.
4. Normalize the result by shifting the mantissa and adjusting the exponent accordingly.
5. Round the result to fit within the format's precision.

#### **_Tricky Things to Remember:_**
- Aligning exponents and normalizing the result is crucial.

***

## Floating Point Subtraction

#### **_Summary:_**
Floating-point subtraction is similar to addition but involves aligning the exponents, subtracting the mantissas, and normalizing the result.

#### **_Definitions:_**
- **Sign Bit**: Indicates the sign of the number.
- **Exponent**: Represents the power of 2.
- **Mantissa**: The fractional part of the number.

#### **_Example:_**
1. Convert both numbers to their IEEE 754 format.
2. Align the exponents by shifting the mantissa of the number with the smaller exponent.
3. Subtract the mantissas.
4. Normalize the result by shifting the mantissa and adjusting the exponent accordingly.
5. Round the result to fit within the format's precision.


#### **_Tricky Things to Remember:_**
- Aligning exponents and normalizing the result is crucial.

***

## Floating Point Division

#### **_Summary:_**
Floating-point division involves dividing the dividend's mantissa by the divisor's mantissa and subtracting the exponents, followed by normalizing.

#### **_Definitions:_**
- **Sign Bit**: Indicates the sign of the number.
- **Exponent**: Represents the power of 2.
- **Mantissa**: The fractional part of the number.

#### **_Example:_**
1. Convert both numbers to their IEEE 754 format.
2. Subtract the exponents and add the bias.
3. Divide the mantissas, including the implicit leading 1.
4. Normalize the result, ensuring that the mantissa fits within the format's precision.
5. Round if necessary, and apply the correct sign.

#### **_Tricky Things to Remember:_**
- Careful handling of the exponent and mantissa is required.

***

## Floating Point Multiplication

#### **_Summary:_**
Floating-point multiplication involves multiplying the mantissas and adding the exponents, followed by normalizing.

#### **_Definitions:_**
- **Sign Bit**: Indicates the sign of the number.
- **Exponent**: Represents the power of 2.
- **Mantissa**: The fractional part of the number.

#### **_Example:_**
1. Convert both numbers to their IEEE 754 format.
2. Add the exponents and subtract the bias (e.g., 127 for single precision).
3. Multiply the mantissas, including the implicit leading 1.
4. Normalize the result, ensuring that the mantissa fits within the format's precision.
5. Round if necessary, and apply the correct sign.


#### **_Tricky Things to Remember:_**
- Proper handling of the exponent and mantissa is required.

***