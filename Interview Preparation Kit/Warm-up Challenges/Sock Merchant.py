from unittest import main, TestCase


def sockMerchant(n, ar):
    socks = set(ar)
    pairs = 0
    for sock in socks:
        number_of_socks = ar.count(sock)
        if number_of_socks % 2 == 0:
            pairs += number_of_socks / 2
        else:
            pairs += (number_of_socks -1) / 2
    return int(pairs)

'''
class sockMerchantTest(TestCase):

    def test_no_sock_pair(self):
        self.assertEqual(sockMerchant(1, [1]), 1)
'''

if __name__ == '__main__':
    #a = sockMerchant(1, [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5, 6, 6, 7, 8, 8])
    a = sockMerchant(1, [1])
    print(a)

    #main()