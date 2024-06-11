import unittest
from task import count_random_number


class MyTestCase(unittest.TestCase):
    def test_count_random_number(self):
        self.assertEqual(count_random_number(),[32, 18, 24, 41, 16, 45, 31, 50, 22, 6])


    def test_find_length(self):
        self.assertEqual(count_random_number(),[32, 18, 24, 41, 16, 45, 31, 50, 22, 6],10)


    def test_sum_even_elements(self):
        self.assertEqual(count_random_number(),[32, 18, 24, 41, 16, 45, 31, 50, 22, 6],168)


    def test_sum_odd_elements(self):
        self.assertEqual(count_random_number(),[32, 18, 24, 41, 16, 45, 31, 50, 22, 6],117)

    def test_multiply_index_element(self):
        self.assertEqual(count_random_number(),[32, 18, 24, 41, 16, 45, 31, 50, 22, 6],{48,90,50})

    def test_average_element(self):
        self.assertEqual(count_random_number(),[32, 18, 24, 41, 16, 45, 31, 50, 22, 6],16.0)

    def test_maximum(self):
        self.assertEqual(count_random_number(),[32, 18, 24, 41, 16, 45, 31, 50, 22, 6],50)

    def test_minimum(self):
        self.assertEqual(count_random_number(),[32, 18, 24, 41, 16, 45, 31, 50, 22, 6],6)


if __name__ == '__main__':
    unittest.main()
