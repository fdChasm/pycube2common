import unittest

from cube2common.string_encoding import decodeutf8, encodeutf8


round_trip_tests = [
    "\x5b\x46\x44\x5d\x43\x68\xc3\x86\x73\x6d\xc3\x80",
]

class StringEncoding(unittest.TestCase):
    def test_one(self):
        src = "\x5b\x46\x44\x5d\x43\x68\xc3\x86\x73\x6d\xc3\x80"
        out = "\x5b\x46\x44\x5d\x43\x68\x07\x73\x6d\x01"

        self.assertEqual(decodeutf8(src), out)

    def test_round_trip(self):
        for src in round_trip_tests:
            self.assertEqual(encodeutf8(decodeutf8(src)), src)

    def test_sauer_code_page_round_trip(self):
        for i in xrange(0, 255):
            src = chr(i)
            self.assertEqual(decodeutf8(encodeutf8(src)), src)
