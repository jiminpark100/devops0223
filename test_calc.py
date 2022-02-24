from unittest import result
import unitest
import calc

class testCals(unitest.TestCase):
    def test_sum(self):
        result=calc.sum(3, 7)
        self.assertEqual(10, result)

    def test_minus(self):
        self.assertEqual(5, calc.minus(10, 5))
