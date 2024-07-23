#!/usr/bin/python3
"""
0-validate_utf8 module
"""


def validUTF8(data):
    """
    Determine if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): A list of integers where each integer represents a byte
        of data.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    num_bytes = 0

    for num in data:
        # Only look at the least significant 8 bits
        byte = num & 0xFF

        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            if byte >> 5 == 0b110:
                num_bytes = 1
            elif byte >> 4 == 0b1110:
                num_bytes = 2
            elif byte >> 3 == 0b11110:
                num_bytes = 3
            elif byte >> 7 != 0:
                return False
        else:
            # Check that the next bytes are of the form 10xxxxxx
            if byte >> 6 != 0b10:
                return False
            num_bytes -= 1

    return num_bytes == 0


if __name__ == "__main__":
    # Test cases
    data1 = [65]
    print(validUTF8(data1))  # Expected: True

    data2 = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108,
             33]
    print(validUTF8(data2))  # Expected: True

    data3 = [229, 65, 127, 256]
    print(validUTF8(data3))  # Expected: False
