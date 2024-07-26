def utfencode(s):
    """Encode a string into UTF-8 bytes.

    Args:
        s (str): The string to encode.

    Returns:
        bytes: The UTF-8 encoded bytes of the string.
    """
    return s.encode("utf-8")


def bin2hex(e):
    """Convert a string to its hexadecimal representation.

    Args:
        e (str): The string to convert.

    Returns:
        str: The hexadecimal representation of the string.
    """
    e = utfencode(e)
    return "".join(format(byte, "02x") for byte in e)


def hex2bin(hex_string):
    """Convert a hexadecimal string back to its original string form.

    Args:
        hex_string (str): The hexadecimal string to convert.

    Returns:
        str: The original string.
    """
    bytes_data = bytes.fromhex(hex_string)
    return bytes_data.decode("utf-8")
