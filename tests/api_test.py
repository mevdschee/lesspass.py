"""lesspass api unit tests"""

import unittest

from lesspass import generate_password

class ApiTests(unittest.TestCase):
    """lesspass api unit test class"""

    def test_default_options(self):
        """test_default_options function"""
        site = 'example.org'
        login = 'contact@example.org'
        master_password = 'password'
        password_profile = {}
        generated_password = generate_password(site, login, master_password, password_profile)
        self.assertEqual('WHLpUL)e00[iHR+w', generated_password)

    def test_no_symbols(self):
        """test_no_symbols function"""
        site = 'example.org'
        login = 'contact@example.org'
        master_password = 'password'
        password_profile = {'length': 14, 'counter': 2, 'symbols': False}
        generated_password = generate_password(site, login, master_password, password_profile)
        self.assertEquals('MBAsB7b1Prt8Sl', generated_password)

    def test_only_digits(self):
        """test_only_digits function"""
        site = 'example.org'
        login = 'contact@example.org'
        master_password = 'password'
        password_profile = {
            'length': 6,
            'counter': 3,
            'lowercase': False,
            'uppercase': False,
            'symbols': False
        }
        generated_password = generate_password(site, login, master_password, password_profile)
        self.assertEquals('117843', generated_password)

    def test_no_numbers(self):
        """test_no_numbers function"""
        site = 'example.org'
        login = 'contact@example.org'
        master_password = 'password'
        password_profile = {'length': 14, 'numbers': False}
        generated_password = generate_password(site, login, master_password, password_profile)
        self.assertEquals('sB>{qF}wN%/-fm', generated_password)

    def test_no_options(self):
        """test_no_options function"""
        site = 'example.org'
        login = 'contact@example.org'
        master_password = 'password'
        generated_password = generate_password(site, login, master_password)
        self.assertEquals('WHLpUL)e00[iHR+w', generated_password)

if __name__ == '__main__':
    unittest.main()
