from pwn import xor

def bytes2matrix(text: bytes) -> list[list[int]]:
    """ Converts a 16-byte array into a 4x4 matrix.  """
    return [list(text[i:i+4]) for i in range(0, len(text), 4)]

def matrix2bytes(matrix: list[list[int]]) -> bytes:
    return_string: bytes = b""
    """ Converts a 4x4 matrix into a 16-byte array.  """
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            return_string += matrix[row][col].to_bytes(length=1, byteorder="big")

    return return_string

def add_round_key(s: list[list[int]], k: list[list[int]]) -> list[list[int]]:
    """XORs the 4xr4 round key to the 4x4 state

    Args:
        s (list[list[int]]): Currents AES state
        k (list[list[int]]): Round key

    Returns:
        list[list[int]]: XOR'd State and Round Key
    """

    assert len(s) == len(k)
    assert len(s[0]) == len(k[0])

    key = matrix2bytes(k)
    state = matrix2bytes(s)

    return bytes2matrix(xor(state, key))
