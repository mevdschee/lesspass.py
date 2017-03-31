"""lesspass entropy unit tests"""

import unittest

from lesspass import get_password_profile
from lesspass import calc_entropy
from lesspass import consume_entropy

class EntropyTests(unittest.TestCase):
    """lesspass entropy unit test class"""

    def test_pbkdf2_with_default_params(self):
        """test_pbkdf2_with_default_params function"""
        site = 'example.org'
        login = 'contact@example.org'
        master_password = 'password'
        password_profile = get_password_profile([])
        entropy = calc_entropy(site, login, master_password, password_profile)
        self.assertEqual(
            'dc33d431bce2b01182c613382483ccdb0e2f66482cbba5e9d07dab34acc7eb1e',
            entropy
        )

    def test_with_different_options(self):
        """test_with_different_options function"""
        site = 'example.org'
        login = 'contact@example.org'
        master_password = 'password'
        password_profile = get_password_profile({
            'iterations': 8192,
            'keylen': 16,
            'digest': 'sha512'
        })
        entropy = calc_entropy(site, login, master_password, password_profile)
        self.assertEqual('fff211c16a4e776b3574c6a5c91fd252', entropy)

    def test_with_counter_one(self):
        """test_with_counter_one function"""
        site = 'example.org'
        login = 'contact@example.org'
        master_password = 'password'
        password_profile = get_password_profile({'iterations': 1, 'keylen': 16})
        entropy = calc_entropy(site, login, master_password, password_profile)
        self.assertEqual('d3ec1e988dd0b3640c7491cd2c2a88b5', entropy)

    def test_with_counter_two(self):
        """test_with_counter_two function"""
        site = 'example.org'
        login = 'contact@example.org'
        master_password = 'password'
        password_profile = get_password_profile({'iterations': 1, 'keylen': 16, 'counter': 2})
        entropy = calc_entropy(site, login, master_password, password_profile)
        self.assertEqual('ddfb1136260f930c21f6d72f6eddbd40', entropy)

    def test_consume_entropy(self):
        """test_consume_entropy function"""
        value, entropy = consume_entropy('', long(4 * 4 + 2), "abcd", 2)
        self.assertEqual('ca', value)
        self.assertEqual(1, entropy)
