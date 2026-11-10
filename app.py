import unittest

# 1. App Logic
def add(a, b):
    return a + b

# 2. Test Cases (No import needed since everything is in one file)
class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(10, 5), 15)
        self.assertEqual(add(-1, 1), 0)

if __name__ == "__main__":
    unittest.main()
