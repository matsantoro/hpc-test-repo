from unittest import TestCase
from SMBC_parse.get_smbc_names import parse_smbc


class TestFunction(TestCase):
    def test_september_2022(self):
        self.assertTrue(len(list(parse_smbc('2022', 'September')))>29) 

