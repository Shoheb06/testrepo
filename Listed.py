

if __name__ == '__main__':
    import unittest

    class TestSingleNonDuplicate(unittest.TestCase):

        def test_single_element(self):
            nums = [1]
            self.assertEqual(Solution().singleNonDuplicate(nums), 1)

        def test_first_element_unique(self):
            nums = [1, 2, 2]
            self.assertEqual(Solution().singleNonDuplicate(nums), 1)

        def test_last_element_unique(self):
            nums = [2, 2, 1]
            self.assertEqual(Solution().singleNonDuplicate(nums), 1)

        def test_middle_element_unique(self):
            nums = [2, 1, 2]
            self.assertEqual(Solution().singleNonDuplicate(nums), 1)

        def test_even_length_array(self):
            nums = [1, 1, 2, 3, 3]
            self.assertEqual(Solution().singleNonDuplicate(nums), 2)

        def test_odd_length_array(self):
            nums = [1, 1, 2, 2, 3]
            self.assertEqual(Solution().singleNonDuplicate(nums), 3)

        def test_example_1(self):
            nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
            self.assertEqual(Solution().singleNonDuplicate(nums), 2)

        def test_example_2(self):
            nums = [3, 3, 7, 7, 10, 11, 11]
            self.assertEqual(Solution().singleNonDuplicate(nums), 10)

    unittest.main()
