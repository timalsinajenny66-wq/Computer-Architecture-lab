# Lab 9: Program to Implement the Booth Algorithm

## Objective

- To understand the Booth multiplication algorithm for signed binary numbers.
- To implement the Booth algorithm using Python.
- To verify the correctness of the multiplication result using test cases.

---

# Theory

The **Booth Algorithm**, introduced by Andrew D. Booth in 1951, is an efficient algorithm used to multiply two signed binary numbers represented in **two's complement** form. Unlike the conventional shift-and-add multiplication method, Booth's algorithm minimizes the number of addition and subtraction operations by detecting consecutive sequences of `1`s in the multiplier.

The algorithm examines the least significant bit (Q₀) of the multiplier together with an extra bit (Q₋₁). Based on these two bits, it decides whether to perform addition, subtraction, or no arithmetic operation before performing an arithmetic right shift. This process is repeated for the number of bits in the operands.

Booth's algorithm supports both positive and negative integers and is widely used in computer architecture because of its efficiency in signed multiplication.

---

# Algorithm

Given multiplicand **M** and multiplier **Q**, each consisting of **n** bits:

1. Initialize:
   - Accumulator **A = 0**
   - **Q₋₁ = 0**
   - Step count = **n**

2. Examine the pair **(Q₀, Q₋₁)**.

| Q₀ | Q₋₁ | Operation |
|:--:|:---:|-----------|
| 0 | 0 | No operation |
| 0 | 1 | A = A + M |
| 1 | 0 | A = A − M |
| 1 | 1 | No operation |

3. Perform an arithmetic right shift on the combined register **[A, Q, Q₋₁]**.

4. Repeat Steps 2 and 3 for **n** iterations.

5. The final product is obtained by combining **[A, Q]**.

---

# Output
```
Please enter your Multiplicand: 9
Please enter your Multiplier: -9
Step  Operation          A         Q  Q-1
init            00000000  11110111  0
1     A - M     11111011  11111011  1
2     no-op     11111101  11111101  1
3     no-op     11111110  11111110  1
4     A + M     00000011  11111111  0
5     A - M     11111101  01111111  1
6     no-op     11111110  10111111  1
7     no-op     11111111  01011111  1
8     no-op     11111111  10101111  1

Decimal Result: -81
Verification (m*q): -81
```

# Discussion

The Booth multiplication algorithm improves multiplication efficiency by reducing unnecessary addition and subtraction operations. Instead of processing each bit independently, it identifies consecutive runs of `1`s in the multiplier and replaces multiple additions with a single subtraction followed by a later addition. This optimization decreases the total number of arithmetic operations, making the algorithm faster than the traditional shift-and-add multiplication method for many input combinations.

The implementation correctly handles both positive and negative integers using two's complement representation. During execution, the algorithm repeatedly checks the pair `(Q₀, Q₋₁)` to determine the required arithmetic operation, performs an arithmetic right shift, and updates the registers until all iterations are completed. The final contents of registers **A** and **Q** represent the signed multiplication result.

The obtained output can be verified by comparing it with the result produced by the normal multiplication operator (`*`) in Python, confirming the correctness of the implementation.

---

# Conclusion

The Booth multiplication algorithm was successfully implemented and tested. The program correctly performs signed binary multiplication using two's complement representation while reducing the number of addition and subtraction operations. The experimental results matched the expected multiplication results, demonstrating the correctness and efficiency of the algorithm. This experiment provides a practical understanding of signed binary multiplication techniques used in computer architecture and digital systems.

---