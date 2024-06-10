import unittest
from addup import my_length


class MyTest_My_length(unittest.TestCase):
    def test_that_function_return_collection_length(self):
        self.assertEqual(my_length([1,2, "semicolon"]), 3)
        self.assertEqual(my_length([]), 0)



        def test_that_function_throws_exception(self):
            self.assertRaises(ValueError,my_length,0)


if __name__ == '__main__':
    unittest.main()
