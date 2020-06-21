import unittest
from math import pi
from Circle import Kolo
r = 5
class CircleTest(unittest.TestCase):
    def setUp(self):
        self.cvt = Kolo(r)

    def test_value_0(self):
        self.assertEqual(self.cvt.pole(), 0)

    def test_value_1(self):
        self.assertEqual(self.cvt.pole(), pi)

    def test_value_2(self):
        self.assertEqual(self.cvt.pole(), 0.1)

    def test_AssertRaisedType(self):
        self.assertRaises(TypeError,self.cvt.r , '1')

    def test_AssertRaisedValue(self):
        self.assertRaises(ValueError, self.cvt.r , 6)



if __name__ == '__main__':
    unittest.main()