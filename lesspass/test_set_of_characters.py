"""lesspass set of characters unit tests"""

import unittest

from .lesspass import _get_set_of_characters
from .lesspass import _get_one_char_per_rule
from .lesspass import _get_configured_rules

class SetOfCharactersTests(unittest.TestCase):
    """lesspass set of characters unit test class"""

    def test_get_default_characters(self):
        """test_get_default_characters function"""
        set_of_characters = _get_set_of_characters()
        self.assertEqual(
            'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789' +
            '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~',
            set_of_characters
        )
        self.assertEqual(26 * 2 + 10 + 32, len(set_of_characters))

    def test_concat_rules_in_order(self):
        """test_concat_rules_in_order function"""
        set_of_characters = _get_set_of_characters(['lowercase', 'uppercase', 'numbers'])
        self.assertEqual(
            'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789',
            set_of_characters
        )
        self.assertEqual(26 * 2 + 10, len(set_of_characters))

    def test_only_lowercase(self):
        """test_only_lowercase function"""
        set_of_characters = _get_set_of_characters(['lowercase'])
        self.assertEqual('abcdefghijklmnopqrstuvwxyz', set_of_characters)
        self.assertEqual(26, len(set_of_characters))

    def test_only_uppercase(self):
        """test_only_uppercase function"""
        set_of_characters = _get_set_of_characters(['uppercase'])
        self.assertEqual('ABCDEFGHIJKLMNOPQRSTUVWXYZ', set_of_characters)
        self.assertEqual(26, len(set_of_characters))

    def test_only_numbers(self):
        """test_only_numbers function"""
        set_of_characters = _get_set_of_characters(['numbers'])
        self.assertEqual('0123456789', set_of_characters)
        self.assertEqual(10, len(set_of_characters))

    def test_only_symbols(self):
        """test_only_symbols function"""
        set_of_characters = _get_set_of_characters(['symbols'])
        self.assertEqual('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~', set_of_characters)
        self.assertEqual(32, len(set_of_characters))

    def test_one_char_per_rule(self):
        """test_one_char_per_rule function"""
        value, entropy = _get_one_char_per_rule(int(26 * 26), ['lowercase', 'uppercase'])
        self.assertEqual('aA', value)
        self.assertEqual(2, len(value))
        self.assertEqual(1, entropy)

    def test_configured_rules(self):
        """test_configured_rules function"""
        self.assertEqual(['uppercase'], _get_configured_rules({
            'uppercase': True}))
        self.assertEqual(['lowercase', 'uppercase'], _get_configured_rules({
            'uppercase': True, 'lowercase': True}))
        self.assertEqual(['lowercase'], _get_configured_rules({
            'lowercase': True, 'symbols': False}))
        self.assertEqual(['lowercase', 'uppercase', 'numbers', 'symbols'], _get_configured_rules({
            'lowercase': True, 'uppercase': True, 'symbols': True, 'numbers': True}))
