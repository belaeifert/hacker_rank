from unittest import TestCase, main


def jumpingOnClouds(clouds):
    emma_position = 0
    jumps = 0

    while emma_position < len(clouds):
        print('Posição: {}. Nuvem: {}'.format(emma_position, clouds[emma_position]))

        # verifica o proximo passo
        if clouds[emma_position+1] == 0:
            jumps += 1

        if clouds[emma_position+2] == 0:
            jumps += 1



    return jumps
'''
class jumpingOnCloudsTest(TestCase):
    def test_sample_case_0(self):
        self.assertEqual(jumpingOnClouds([0, 1, 0, 0, 0, 1, 0], 1))
'''
if __name__ == '__main__':
    #main()
    jumpingOnClouds([0, 1, 0,  0, 0, 1, 0])