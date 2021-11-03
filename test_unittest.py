from unittest import TestCase

class Mytest(TestCase):
    def test_one_plus_two(self):
        self.assertEqual(1+2,5)
