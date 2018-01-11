import unittest
# from paymentdates import payTime
from paydatesidea import payTime
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

    def test_period_monthly(self):
        expectedResult = [[date(2015, 04, 23), date(2015, 04, 30)], [date(2015, 05, 01), date(2015, 05, 30)]]
        self.assertEqual(payTime('2015-04-23', '2015-05-30', 'unadjusted', 'monthly'), expectedResult)

    def test_period_bimonthly(self):
        expectedResult = [[date(2015, 04, 02), date(2015, 04, 15)], [date(2015, 04, 16), date(2015, 04, 30)]]
        self.assertEqual(payTime('2015-04-02', '2015-04-30', 'unadjusted', 'bimonthly'), expectedResult)

    def test_close_bimonthly(self):
        expectedResult = [[date(2015, 04, 02), date(2015, 04, 16)]]
        self.assertEqual(payTime('2015-04-02', '2015-04-16', 'unadjusted', 'bimonthly'), expectedResult)

    def test_annually_period(self):
        expectedResult = [[date(2014, 04, 03), date(2014, 12, 31)], [date(2015, 01, 01), date(2015, 02, 05)]]
        self.assertEqual(payTime('2014-04-03', '2015-02-05', 'unadjusted', 'annually'), expectedResult)

    def test_period_biannually(self):
        expectedResult = [[date(2014, 04, 03), date(2014, 06, 30)], [date(2014, 07, 01), date(2014, 12, 31)], [date(2015, 01, 01), date(2015, 06, 27)]]
        self.assertEqual(payTime('2014-04-03', '2015-06-27', 'unadjusted', 'biannually'), expectedResult)

    def test_convention_adjusted(self):
        expectedResult =[[date(2004, 03, 15), date(2004, 03, 31)], [date(2004, 04, 01), date(2004, 04, 30)], [date(2004, 05, 03), date(2004, 05, 25)]]
        self.assertEqual(payTime('2004-03-14', '2004-05-25', 'adjusted', 'monthly'), expectedResult)

    # add test for adjusted using calendar monthrange func[0] and 1day til its a businss day
    # this change canjust be added onto removal/sorting part of paydateside

if __name__ == '__main__':
    unittest.main()
