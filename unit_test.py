# def test_sum():
#     assert sum([1,2,3]) == 6

# def test_sum_tuple():
#     assert sum((1,2,2,)) == 6 


# if __name__ == '__main__':
#     test_sum()
#     test_sum_tuple()
#     print('Everything Passed')


import unittest


class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, )

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 5, )


if __name__ == '__main__':
    unittest.main()
