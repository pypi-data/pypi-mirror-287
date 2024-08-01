import unittest
from textstyler.banner import CreateBanner

class TestBanner(unittest.TestCase):
    def test_create_banner(self):
        banner = CreateBanner("Hello")
        self.assertTrue(banner.startswith(" _    _"))
        self.assertTrue("Hello" in banner)

if __name__ == '__main__':
    unittest.main()
