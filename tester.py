import numpy as np

white_threat = np.full((8,8), 0b0000000000000100)


def is_bit_one(number: int, position: int) -> bool:
    mask = 1 << (position)
    return (number & mask) != 0

number = 1 << 4

mask = 0

print(bin(number | mask))