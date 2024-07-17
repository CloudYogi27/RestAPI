'''
Sample Test
'''

from django.test import SimpleTestCase

from app import calc


class CalcTest(SimpleTestCase):

    def test_add_number(self):
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_sub_number(self):
        res = calc.sub(10, 5)
        self.assertEqual(res, 5)

    def test_mul_number(self):
        res = calc.mul(5, 6)
        self.assertEqual(res, 30)
