

def decode(buffer: bytearray, offset: int=0, max_length: int=0) -> int:
    return buffer, offset, max_length


def encode(content: int) -> bytearray:
    if content < 0 or type(content) != int:
        raise ValueError("Invalid content")

    flag = 0
    done = False
    ret_array = bytearray()
    while not done:
        new_bits = content & 0x7F
        content >>= 7
        ret_array.append(new_bits + flag)
        if flag == 0:
            flag = 0x80
        if content == 0:
            done = True

    ret_array.reverse()
    return ret_array

