from unittest import TestCase, main


def birthdayCakeCandles(ar):
    return ar.count(max((ar)))


class birthdayCakeCandlesTest(TestCase):

    def testOneYearBirthday(self):
        arr = birthdayCakeCandles([1])
        self.assertEqual(arr, 1)

    def testTwoYearsBirthday(self):
        ''' Just one candle is taller'''
        arr = birthdayCakeCandles([1, 2])
        self.assertEqual(arr, 1)

    def testTwoYearsBirthdayTwo(self):
        ''' The candles are the same height'''
        arr = birthdayCakeCandles([2, 2])
        self.assertEqual(arr, 2)

    def testThreeYearsBirthday1(self):
        ''' The candles are the same height'''
        arr = birthdayCakeCandles([3, 2, 1])
        self.assertEqual(arr, 1)

    def testTenYearsBirthday1(self):
        arr = birthdayCakeCandles([44, 53, 31, 27, 77, 60, 66, 77, 26, 36])
        self.assertEqual(arr, 2)

    def testTenYearsBirthday2(self):
        arr = birthdayCakeCandles([18, 90, 90, 13, 90, 75, 90, 8, 90, 43])
        self.assertEqual(arr, 5)



if __name__ == '__main__':
    main()


