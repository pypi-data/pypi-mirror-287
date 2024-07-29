import unittest

from src.mult.mult3 import multiply_by_three

class TMBT(unittest.TestCase):

	def test_multiply_by_three(self):
		self.assertEqual(multiply_by_three(4), 12)

if __name__ == '__main__':
    unittest.main()