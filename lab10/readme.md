# Lab 10: Program to Implement the Non-Restoring Division Algorithm

## Objective

- To understand the Non-Restoring Division algorithm for unsigned binary numbers.
- To implement the Non-Restoring Division algorithm using Python.
- To verify the correctness of the quotient and remainder through test cases.

---

# Theory

The **Non-Restoring Division Algorithm** is an efficient binary division technique used in computer architecture for dividing unsigned binary numbers. It eliminates the restoration step required in the restoring division algorithm, thereby reducing the number of arithmetic operations and improving execution efficiency.

The algorithm uses three registers:

- **A** – Partial remainder register
- **Q** – Dividend and quotient register
- **M** – Divisor register

Initially, the partial remainder register (**A**) is set to zero, while the dividend is loaded into the quotient register (**Q**). During each iteration, the combined registers **[A, Q]** are shifted left by one bit.

The sign of the partial remainder determines the arithmetic operation:

- If **A ≥ 0**, subtract the divisor (**A = A − M**).
- If **A < 0**, add the divisor (**A = A + M**).

After the operation, the least significant bit of the quotient is updated according to the sign of **A**.

Unlike restoring division, the algorithm does not immediately restore the partial remainder after a negative result. Instead, it carries the negative remainder into the next iteration and performs a final correction only if necessary after all iterations are completed.

---

# Algorithm

Given dividend **Q** (n bits) and divisor **M** (n bits), both unsigned:

1. Initialize:
   - Set **A = 0**
   - Load the dividend into **Q**

2. Repeat the following for **n** iterations:

   a. Left shift the combined registers **[A, Q]** by one bit.

   b. Perform one of the following operations:
   - If **A ≥ 0**, subtract the divisor:
     - **A = A − M**
   - If **A < 0**, add the divisor:
     - **A = A + M**

   c. Set the least significant bit of **Q**:
   - If **A ≥ 0**, set **Q₀ = 1**
   - If **A < 0**, set **Q₀ = 0**

3. After completing all iterations:
   - If **A < 0**, perform the final correction:
     - **A = A + M**

4. The final values are:
   - **Q** → Quotient
   - **A** → Remainder

---

# Output
```
Enter Dividend (Decimal): 88
Enter Divisor (Decimal): 8

Initial Values
A = 00000000
Q = 01011000
M = 00001000

Step 1
Shift Left & Subtract M
A = 11111000
Q = 10110000

Step 2
Shift Left & Add M
A = 11111001
Q = 01100000

Step 3
Shift Left & Add M
A = 11111010
Q = 11000000

Step 4
Shift Left & Add M
A = 11111101
Q = 10000000

Step 5
Shift Left & Add M
A = 00000011
Q = 00000001

Step 6
Shift Left & Subtract M
A = 11111110
Q = 00000010

Step 7
Shift Left & Add M
A = 00000100
Q = 00000101

Step 8
Shift Left & Subtract M
A = 00000000
Q = 00001011

-----------------------------------
Binary Quotient : 00001011
Decimal Quotient: 11
Binary Remainder: 00000000
Decimal Remainder: 0
```

# Discussion

The Non-Restoring Division algorithm provides an efficient method for performing binary division by avoiding the repeated restoration step used in the restoring division algorithm. Instead of restoring the partial remainder whenever it becomes negative, the algorithm postpones the correction until the end of the computation. This approach reduces the number of arithmetic operations and improves computational efficiency.

In this implementation, the algorithm repeatedly shifts the combined registers **[A, Q]**, performs either subtraction or addition based on the sign of the partial remainder, and updates the quotient bit accordingly. If the partial remainder is negative after all iterations, a final correction is performed by adding the divisor back to obtain the correct remainder.

The generated quotient and remainder were verified using standard division results, confirming the correctness of the implementation. The experiment demonstrates how arithmetic operations at the hardware level can be optimized through algorithmic improvements.

---

# Conclusion

The Non-Restoring Division algorithm was successfully implemented and tested using Python. The program correctly computes the quotient and remainder for unsigned binary division while minimizing unnecessary restoration operations. The results matched the expected outputs obtained through conventional division, validating the correctness of the implementation. This experiment enhances the understanding of binary arithmetic algorithms and their application in processor design and computer architecture.

---
