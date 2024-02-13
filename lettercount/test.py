import unittest
from problem import letter_count

class TestSolution(unittest.TestCase):
    def first_word(self):
       self.assertEqual(letter_count('Hello apple pie'), 'Hello', f'expected "Hello" but got {letter_count("Hello apple pie")}')
       self.assertEqual(letter_count("good luck"), "good", f'Wrong: got {letter_count("good luck")}')

    def word_bob(self):
        self.assertEqual(letter_count('i went to see bob'), 'bob', f'expected "bob" but got {letter_count(" i went to see bob ")}')
        self.assertEqual(letter_count('dad went to go see bob'), 'dad', f'expected "dad" but got {letter_count("dad went to go see bob")}')

    def word_with_special_characters(self):
        self.assertEqual(letter_count('lee\'paul! was happy to see me'), 'lee\'paul', f'expected "lee\'paul" but got {letter_count("lee'paul! was happy to see me")}')
        self.assertEqual(letter_count('bob\'s parent\'s didn\'t love him'), 'bob', f'expected "bob" but got {letter_count("bob parent's didn't love him")}')

    def double_and_triple(self):
        self.assertEqual(letter_count("Bob and bobbie ate lollies"), 'bobbie', f'expected "bobbie" but got {letter_count("Bob and bobbie ate lollies")}')
if __name__ == "__main__":
    unittest.main()