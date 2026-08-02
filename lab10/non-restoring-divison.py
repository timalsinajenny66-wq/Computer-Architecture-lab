def add(A, M):
    carry = 0
    result = ""

    for i in range(len(A) - 1, -1, -1):
        temp = int(A[i]) + int(M[i]) + carry
        result = str(temp % 2) + result
        carry = temp // 2

    return result


def compliment(m):
    # 2's complement
    inverted = "".join("1" if b == "0" else "0" for b in m)
    one = "0" * (len(m) - 1) + "1"
    return add(inverted, one)


def nonRestoringDivision(dividend_dec, divisor_dec):
    bit_len = max(dividend_dec.bit_length(), divisor_dec.bit_length()) + 1

    Q = format(dividend_dec, f"0{bit_len}b")
    M = format(divisor_dec, f"0{bit_len}b")
    A = "0" * bit_len

    comp_M = compliment(M)
    flag = "successful"

    print(f"\nInitial Values")
    print(f"A = {A}")
    print(f"Q = {Q}")
    print(f"M = {M}")

    for step in range(1, bit_len + 1):
        print(f"\nStep {step}")

        # Left Shift of A,Q
        combined = (A + Q)[1:]

        A = combined[:bit_len]
        Q_temp = combined[bit_len:]

        # Pad Q_temp back to bit_len-1 bits
        Q_temp = Q_temp.zfill(bit_len - 1)

        if flag == "successful":
            A = add(A, comp_M)
            print("Shift Left & Subtract M")
        else:
            A = add(A, M)
            print("Shift Left & Add M")

        if A[0] == "1":
            Q = Q_temp + "0"
            flag = "unsuccessful"
        else:
            Q = Q_temp + "1"
            flag = "successful"

        print(f"A = {A}")
        print(f"Q = {Q}")

    # Final correction
    if A[0] == "1":
        print("\nFinal Correction: A = A + M")
        A = add(A, M)

    print("\n" + "-" * 35)
    print(f"Binary Quotient : {Q}")
    print(f"Decimal Quotient: {int(Q, 2)}")
    print(f"Binary Remainder: {A}")
    print(f"Decimal Remainder: {int(A, 2)}")


if __name__ == "__main__":
    try:
        dividend = int(input("Enter Dividend (Decimal): "))
        divisor = int(input("Enter Divisor (Decimal): "))

        if divisor == 0:
            print("Division by zero is not allowed.")
        else:
            nonRestoringDivision(dividend, divisor)

    except ValueError:
        print("Please enter valid integers.")
80