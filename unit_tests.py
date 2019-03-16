from unittest import TestCase, main
from docstrings import is_palindrome

class WordsTestCase(TestCase):
    def test_is_palindrome_true(self):
        self.assertEqual(is_palindrome('meem'), True)
    def test_is_palindrome_false(self):
        self.assertEqual(is_palindrome('word'), False)

if __name__ == '__main__':
    main()