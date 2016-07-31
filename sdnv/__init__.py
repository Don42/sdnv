

def decode(buffer: bytearray, offset: int=0, max_length: int=None) -> int:
    content = int()
    for i, c in enumerate(buffer[offset:max_length]):
        content <<= 7
        content += c & 0x7F
        if not 0x80 & c:
            break
    else:
        raise ValueError("Reached end of input without finding end of SDNV")
    return content, i + 1


def encode(content: int) -> bytearray:
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

