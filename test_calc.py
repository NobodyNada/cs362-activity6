import unittest
import calc


class CalcTests(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(1, 2), 3)
        self.assertEqual(calc.add(-1, 3), 2)
        self.assertEqual(calc.add(5, 0), 5)
        self.assertAlmostEqual(calc.add(0.1, 0.2), 0.3)

    def test_sub(self):
        self.assertEqual(calc.sub(3, 2), 1)
        self.assertEqual(calc.sub(2, 3), -1)
        self.assertAlmostEqual(calc.sub(5.5, 0.5), 5)
