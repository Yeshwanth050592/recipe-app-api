from django.test import TestCase

from app.cal import add


class CalcTests(TestCase):

    def test_add_numbers(self):
        """Test that values are added together"""
        self.assertEqual(add(3, 8), 11)