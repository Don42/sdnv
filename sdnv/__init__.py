

def decode(buffer: bytearray, offset: int=0, max_length: int=9) -> (int, int):
    """Decode a SDNV from a buffer

    :param buffer: The buffer which contains a SDNV
    :param offset: The offset into the buffer, at which the SDNV can be found
    :param max_length: The maximum number of octets that make up the SDNV
    :return: Decoded value and number of octets that made up the SDNV
    """
    content = int()
    for i, c in enumerate(buffer[offset:offset+max_length]):
        content <<= 7
        content += c & 0x7F
        if not 0x80 & c:
            break
    else:
        raise ValueError("Reached end of input without finding end of SDNV")
    return content, i + 1


def encode(content: int) -> bytearray:
    """Encode an integer into a SDNV

    :param content: Integer to encode
    :return: Bytearray containing the encoded value
    """
    if content < 0 or type(content) != int:
        raise ValueError("Invalid content")

    flag = 0
    ret_array = bytearray()
    while True:
        new_bits = content & 0x7F
        content >>= 7
        ret_array.append(new_bits + flag)
        if flag == 0:
            flag = 0x80
        if content == 0:
            break

    ret_array.reverse()
    return ret_array

