import unittest
from textstyler.styler import StyleText

class TestStyler(unittest.TestCase):
    def test_style_text(self):
        styled = StyleText("Hello", color="red", on_color="on_yellow", attrs=["bold"])
        self.assertIn("\033[1m", styled)
        self.assertIn("\033[31m", styled)
        self.assertIn("\033[43m", styled)

if __name__ == '__main__':
    unittest.main()
