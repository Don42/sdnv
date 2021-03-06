import unittest
from ddt import ddt, data as ddt_data

import sdnv

data = ((0xABC, [0x95, 0x3C]),
        (0x1234, [0xA4, 0x34]),
        (0x4234, [0x81, 0x84, 0x34]),
        (0x7F, [0x7F]),
        (0x44, [0x44]))


@ddt
class SDNVTest(unittest.TestCase):
    @ddt_data(*data)
    def test_encode(self, val_pair: tuple):
        expected = bytearray(val_pair[1])
        result = sdnv.encode(val_pair[0])
        if expected != result:
            print(expected, result, expected == result)
            print(bytes(expected), bytes(result))
            raise AssertionError("Result does not match expectations, %s != %s", result, expected)

    @ddt_data(*data)
    def test_decode(self, val_pair: tuple):
        expected = val_pair[0]
        result = sdnv.decode(bytearray(val_pair[1]))
        self.assertEqual(result[0], expected)
        self.assertEqual(result[1], len(val_pair[1]))

