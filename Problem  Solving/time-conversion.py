from unittest import TestCase, main


def timeConversion(s):
    hour, period = s[0:2], s[-2:]
    if period == 'PM' and hour != '12':
        hour = int(hour) + 12
    elif period == 'AM' and hour == '12':
        hour = '00'
    return str(hour)+s[2:-2]


class timeConversionTest(TestCase):
    def testconvertingTimePM(self):
        self.assertEqual(timeConversion('07:05:45PM'), '19:05:45')

    def testconvertingTimeAM(self):
        self.assertEqual(timeConversion('07:05:45AM'), '07:05:45')

    def testMidNight(self):
        self.assertEqual(timeConversion('12:40:22AM'), '00:40:22')

    def testMidDay(self):
        self.assertEqual(timeConversion('12:40:22PM'), '12:40:22')


if __name__ == '__main__':
    main()
    print(timeConversion('07:05:45PM'))