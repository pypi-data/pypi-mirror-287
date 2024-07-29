import unittest

from src.div.div3 import divide_by_three

class TDBT(unittest.TestCase):

	def test_divide_by_three(self):
		self.assertEqual(divide_by_three(12), 4)

if __name__ == '__main__':
    unittest.main()