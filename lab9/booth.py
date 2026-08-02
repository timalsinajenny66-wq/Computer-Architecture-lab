

def booths_algorithm(multiplicand, multiplier, bits=8):
    """
    Multiplies two signed integers using Booth's algorithm.
    bits = word size (default 8-bit, matching range -128..127)
    """
    mask = (1 << bits) - 1

    # Product register layout: [A (bits)] [Q (bits)] [Q-1 (1 bit)]
    A = 0
    Q = multiplier & mask
    Q_1 = 0
    M = multiplicand & mask

    def to_signed(val, width):
        if val & (1 << (width - 1)):
            val -= (1 << width)
        return val

    print(f"{'Step':<6}{'Operation':<10}{'A':>10}{'Q':>10}{'Q-1':>5}")
    print(f"{'init':<6}{'':<10}{A:0{bits}b}{'':>2}{Q:0{bits}b}{'':>2}{Q_1}")

    for step in range(1, bits + 1):
        last_two = (Q & 1, Q_1)

        if last_two == (1, 0):      # 10 -> subtract
            A = (A - M) & mask
            op = "A - M"
        elif last_two == (0, 1):    # 01 -> add
            A = (A + M) & mask
            op = "A + M"
        else:                       # 00 or 11 -> no-op
            op = "no-op"

        # Arithmetic right shift of {A, Q, Q-1}
        combined = (A << (bits + 1)) | (Q << 1) | Q_1
        sign_bit = (A >> (bits - 1)) & 1
        combined >>= 1
        combined |= sign_bit << (2 * bits)   # preserve sign in shift

        Q_1 = (combined >> 0) & 1
        Q = (combined >> 1) & mask
        A = (combined >> (bits + 1)) & mask

        print(f"{step:<6}{op:<10}{A:0{bits}b}{'':>2}{Q:0{bits}b}{'':>2}{Q_1}")

    result = to_signed((A << bits) | Q, 2 * bits)
    return result


def get_input(name, bits=8):
    lo, hi = -(1 << (bits - 1)), (1 << (bits - 1)) - 1

    val = int(input(f"Please enter your {name}: "))

    while not (lo <= val <= hi):
        print(f"Value out of range ({lo} to {hi}), please try again")
        val = int(input(f"Please enter your {name}: "))

    return val


if __name__ == "__main__":
    m = get_input("Multiplicand")
    q = get_input("Multiplier")

    result = booths_algorithm(m, q)

    print(f"\nDecimal Result: {result}")
    print(f"Verification (m*q): {m * q}")


