import unittest
from src.mapping_to_single import map_brightness_char

class Test_one(unittest.TestCase):
    def test_map_bright_char(self):
        self.assertEqual(map_brightness_char(255),' ')

if __name__ == '__main__':
    unittest.main()