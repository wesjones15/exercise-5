import unittest
# from paymentdates import payTime
from paydatesidea import payTime
from datetime import datetime, date
import calendar

class PayTestCase(unittest.TestCase):

    def test_dad_ex(self):
        expectedResult = [[date(2017, 01, 03), date(2017, 02, 02)], [date(2017, 02, 03), date(2017, 03, 02)], [date(2017, 03, 03), date(2017, 03, 31)]]
        self.assertEqual(payTime('2017-01-03', '2017-03-31', 'unadjusted', 'monthly', 'date'), expectedResult)

    def test_proper_adjusted(self):
        expectedResult = [[date(2017, 03, 03), date(2017, 04, 03)], [date(2017, 04, 04), date(2017, 05, 02)], [date(2017, 05, 03), date(2017, 06, 01)]]
        self.assertEqual(payTime('2017-03-03', '2017-06-01', 'following', 'monthly', 'date'), expectedResult)

    def test_partial_month(self):
        expectedResult = [[date(2017, 01, 01), date(2017, 01, 15)]]
        self.assertEqual(payTime('2017-01-01', '2017-01-15', 'unadjusted', 'monthly', 'date'), expectedResult)

    def test_full_month(self):
        expectedResult = [[date(2017, 01, 01), date(2017, 01, 30)]]
        self.assertEqual(payTime('2017-01-01', '2017-01-30', 'unadjusted', 'monthly', 'date'), expectedResult)

    def test_multiple_months(self):
        expectedResult = [[date(2017, 01, 01), date(2017, 01, 31)], [date(2017, 02, 01), date(2017, 02, 28)]]
        self.assertEqual(payTime('2017-01-01', '2017-02-28', 'unadjusted', 'monthly', 'date'), expectedResult)

    def test_two_years(self):
        expectedResult = [[date(2017, 12, 01), date(2017, 12, 31)], [date(2018, 01, 01), date(2018, 01, 18)]]
        self.assertEqual(payTime('2017-12-01', '2018-01-18', 'unadjusted', 'monthly', 'date'), expectedResult)

    def test_many_years(self):
        expectedResult = [[date(2014, 12, 02), date(2015, 01, 01)], [date(2015, 01, 02), date(2015, 02, 01)], [date(2015, 02, 02), date(2015, 02, 15)]]
        self.assertEqual(payTime('2014-12-02', '2015-02-15', 'unadjusted', 'monthly', 'date'), expectedResult)

    def test_period_monthly(self):
        expectedResult = [[date(2015, 04, 23), date(2015, 05, 22)], [date(2015, 05, 23), date(2015, 05, 30)]]
        self.assertEqual(payTime('2015-04-23', '2015-05-30', 'unadjusted', 'monthly', 'date'), expectedResult)

    def test_period_bimonthly(self):
        expectedResult = [[date(2015, 04, 02), date(2015, 04, 16)], [date(2015, 04, 17), date(2015, 04, 30)]]
        self.assertEqual(payTime('2015-04-02', '2015-04-30', 'unadjusted', 'bimonthly', 'date'), expectedResult)

    def test_close_bimonthly(self):
        expectedResult = [[date(2015, 04, 02), date(2015, 04, 16)]]
        self.assertEqual(payTime('2015-04-02', '2015-04-16', 'unadjusted', 'bimonthly', 'date'), expectedResult)

    def test_annually_period(self):
        expectedResult = [[date(2014, 04, 07), date(2015, 04, 06)], [date(2015, 04, 07), date(2015, 07, 19)]]
        self.assertEqual(payTime('2014-04-07', '2015-07-19', 'unadjusted', 'annually', 'date'), expectedResult)

    def test_annual_period(self):
        expectedResult = [[date(2014, 04, 07), date(2015, 04, 06)], [date(2015, 04, 07), date(2016, 02, 05)]]
        self.assertEqual(payTime('2014-04-07', '2016-02-05', 'unadjusted', 'annually', 'date'), expectedResult)

    # add test for annual adjusted

    def test_period_biannually(self):
        expectedResult = [[date(2014, 04, 03), date(2014, 10, 02)], [date(2014, 10, 03), date(2015, 04, 02)], [date(2015, 04, 03), date(2015, 06, 27)]]
        self.assertEqual(payTime('2014-04-03', '2015-06-27', 'unadjusted', 'biannually', 'date'), expectedResult)

    def test_convention_reg_following(self):
        expectedResult = [[date(2018, 03, 01), date(2018, 04, 02)], [date(2018, 04, 03), date(2018, 04, 30)], [date(2018, 05, 01), date(2018, 05, 31)]]
        self.assertEqual(payTime('2018-03-01', '2018-05-31', 'following', 'monthly', 'date'), expectedResult)

    def test_convention_modified_following(self):
        expectedResult = [[date(2018, 3, 1), date(2018, 3, 30)], [date(2018, 3, 31), date(2018, 4, 30)], [date(2018, 5, 1), date(2018, 5, 31)]]
        self.assertEqual(payTime('2018-03-01', '2018-05-31', 'modified following', 'monthly', 'date'), expectedResult)

    # add test for adjusted using calendar monthrange func[0] and 1day til its a businss day
    # this change canjust be added onto removal/sorting part of paydateside

# if __name__ == '__main__':
#     unittest.main()
