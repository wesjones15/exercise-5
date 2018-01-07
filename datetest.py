import unittest
from paymentdates import payTime
from datetime import datetime, date
import calendar

class PayTestCase(unittest.TestCase):

    def test_partial_month(self):
        expectedResult = [[date(2017, 01, 01), date(2017, 01, 15)]]
        self.assertEqual(payTime('2017-01-01', '2017-01-15', 'unadjusted', 'monthly'), expectedResult)

    def test_full_month(self):
        expectedResult = [[date(2017, 01, 01), date(2017, 01, 30)]]
        self.assertEqual(payTime('2017-01-01', '2017-01-30', 'unadjusted', 'monthly'), expectedResult)

    def test_multiple_months(self):
        expectedResult = [[date(2017, 01, 01), date(2017, 01, 31)], [date(2017, 02, 01), date(2017, 02, 28)]]
        self.assertEqual(payTime('2017-01-01', '2017-02-28', 'unadjusted', 'monthly'), expectedResult)

    def test_two_years(self):
        expectedResult = [[date(2017, 12, 01), date(2017, 12, 31)], [date(2018, 01, 01), date(2018, 01, 18)]]
        self.assertEqual(payTime('2017-12-01', '2018-01-18', 'unadjusted', 'monthly'), expectedResult)

    def test_many_years(self):
        expectedResult = [[date(2014, 12, 02), date(2014, 12, 31)], [date(2015, 01, 01), date(2015, 01, 31)], [date(2015, 02, 01), date(2015, 02, 15)]]
        self.assertEqual(payTime('2014-12-02', '2015-02-15', 'unadjusted', 'monthly'), expectedResult)
    # test over year boundary

if __name__ == '__main__':
    unittest.main()
