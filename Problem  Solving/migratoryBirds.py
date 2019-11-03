from unittest import TestCase, main


def migratoryBirds(birds):
    return max(set(birds), key=birds.count)


class MigratoryBirdsTest(TestCase):

    def testMigrationBirds(self):
        self.assertEqual(migratoryBirds([1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]), 3)

if __name__ == '__main__':
    #main()
    print(migratoryBirds([1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4, 4, 4, 4]))