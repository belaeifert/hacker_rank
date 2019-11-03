from unittest import TestCase, main


def countingValleys(n, hike):
    lvl = 1
    valleys = 0
    for step in hike:
        if step == 'U':
           lvl += 1
        else:
            lvl -= 1
            if lvl == 0:
                valleys += 1
    return valleys


class countingValleysTest(TestCase):

    def test_sample_case_0(self):
        self.assertEqual(countingValleys(8, 'UDDDUDUU'), 1)

    def test_sample_case_1(self):
        self.assertEqual(countingValleys(12, 'DDUUDDUDUUUD'), 2)


if __name__ == '__main__':
    main()
