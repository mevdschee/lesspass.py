"""lesspass render password unit tests"""

import unittest

from .lesspass import _get_password_profile
from .lesspass import _render_password
from .lesspass import _insert_string_pseudo_randomly

class RenderPasswordTests(unittest.TestCase):
    """lesspass render password unit test class"""

    def test_remainder_as_index(self):
        """test_remainder_as_index function"""
        entropy = 'dc33d431bce2b01182c613382483ccdb0e2f66482cbba5e9d07dab34acc7eb1e'
        password_profile = _get_password_profile([])
        self.assertEqual('W', _render_password(entropy, password_profile)[0])


    def test_quotient_as_second_entropy(self):
        """test_quotient_as_second_entropy function"""
        entropy = 'dc33d431bce2b01182c613382483ccdb0e2f66482cbba5e9d07dab34acc7eb1e'
        password_profile = _get_password_profile([])
        self.assertEqual('H', _render_password(entropy, password_profile)[1])


    def test_default_length_sixteen(self):
        """test_default_length_sixteen function"""
        entropy = 'dc33d431bce2b01182c613382483ccdb0e2f66482cbba5e9d07dab34acc7eb1e'
        password_profile = _get_password_profile([])
        self.assertEqual(16, len(_render_password(entropy, password_profile)))


    def test_can_specify_length(self):
        """test_can_specify_length function"""
        entropy = 'dc33d431bce2b01182c613382483ccdb0e2f66482cbba5e9d07dab34acc7eb1e'
        password_profile = _get_password_profile({'length': 20})
        self.assertEqual(20, len(_render_password(entropy, password_profile)))


    def test_one_of_each_set_of_chars(self):
        """test_one_of_each_set_of_chars function"""
        password = _insert_string_pseudo_randomly('123456', int(7 * 6 + 2), 'uT')
        self.assertEqual('T12u3456', password)


    def test_at_least_one_of_each_set(self):
        """test_at_least_one_of_each_set function"""
        entropy = 'dc33d431bce2b01182c613382483ccdb0e2f66482cbba5e9d07dab34acc7eb1e'
        password_profile = _get_password_profile({'length': 6})
        generated_password = _render_password(entropy, password_profile)
        lowercase_ok = False
        uppercase_ok = False
        numbers_ok = False
        symbols_ok = False
        for letter in generated_password:
            if letter in 'abcdefghijklmnopqrstuvwxyz':
                lowercase_ok = True
            if letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                uppercase_ok = True
            if letter in '0123456789':
                numbers_ok = True
            if letter in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~':
                symbols_ok = True
        all_ok = lowercase_ok and uppercase_ok and numbers_ok and symbols_ok
        self.assertEqual(6, len(generated_password))
        self.assertEqual(True, all_ok, 'there is not at least one char in every characters set')
