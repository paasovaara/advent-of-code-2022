import unittest
from main import item_priority

class TestItemPriority(unittest.TestCase):

    def test_lower_case_letters(self):
        self.assertEqual(item_priority('a'), 1)
        self.assertEqual(item_priority('z'), 26)

    def test_upper_case_letters(self):
        self.assertEqual(item_priority('A'), 27)
        self.assertEqual(item_priority('Z'), 52)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            item_priority('1')
        with self.assertRaises(ValueError):
            item_priority('')
        with self.assertRaises(ValueError):
            item_priority('ab')
        with self.assertRaises(ValueError):
            item_priority(None)

if __name__ == '__main__':
    unittest.main()
