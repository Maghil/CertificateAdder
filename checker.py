import unittest
import helper

class checker(unittest.TestCase):
    def test_yaml(self):
        self.assertIsNot(helper.userData(),False)
        self.assertIsNot(helper.certificate(),False)

if __name__ == "__main__":
    unittest.main()