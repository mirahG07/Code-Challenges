""""
Have the function CamelCase(str) take the str parameter being passed and return it in 
proper camel case format where the first letter of each word is capitalized (excluding the first letter). 
The string will only contain letters and some combination of delimiter punctuation characters separating each word.
For example: if str is ""BOB loves-coding"" then your program should return the string bobLovesCoding.

Input: ""cats AND*Dogs-are Awesome""
Output: catsAndDogsAreAwesome
Input: ""a b c d-e-f%g""
Output: aBCDEFG
"""

import unittest
from problems import camel_case

class TestSolution(unittest.TestCase):
    def test_example(self):
        self.assertEqual(camel_case("cats AND*Dogs-are Awesome"),"catsAndDogsAreAwesome", f'Wrong: got {camel_case("cats AND*Dogs-are Awesome")}')
        self.assertEqual(camel_case("a b c d-e-f%g"), "aBCDEFG", f'Wrong: got {camel_case("a b c d-e-f%g")}')
    
    def test_names(self):
        self.assertEqual(camel_case("Tamirah Calloway-Gaines"), "tamirahCallowayGaines", f'Wrong: got {camel_case("Tamirah Calloway-Gaines")}')
        self.assertEqual(camel_case("Lanay Rose"), "LanayRose", f'Wrong: got {camel_case("Lanay Rose")}')

    def test_colors(self):
        self.assertEqual(camel_case("BlUe"), "blue", f'Right: got {camel_case("blue")}')
        self.assertEqual(camel_case("gReEn"), "green", f'Right: got {camel_case("green")}')

if __name__ == "__main__":
    unittest.main()