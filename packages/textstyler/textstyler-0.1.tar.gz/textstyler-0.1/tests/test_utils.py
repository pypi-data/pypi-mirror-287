import unittest
from textstyler.utils import ListFonts

class TestUtils(unittest.TestCase):
    def test_list_fonts(self):
        fonts = ListFonts()
        self.assertTrue(len(fonts) > 0)
        self.assertTrue("standard" in fonts)

if __name__ == '__main__':
    unittest.main()
