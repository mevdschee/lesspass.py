"""lesspass api unit tests"""

from .lesspass import generate_password

def test_default_options():
    """test_default_options function"""
    site = 'example.org'
    login = 'contact@example.org'
    master_password = 'password'
    password_profile = {}
    generated_password = generate_password(site, login, master_password, password_profile)
    assert generated_password == 'WHLpUL)e00[iHR+w'

def test_no_symbols():
    """test_no_symbols function"""
    site = 'example.org'
    login = 'contact@example.org'
    master_password = 'password'
    password_profile = {'length': 14, 'counter': 2, 'symbols': False}
    generated_password = generate_password(site, login, master_password, password_profile)
    assert generated_password == 'MBAsB7b1Prt8Sl'

def test_only_digits():
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
    assert generated_password == '117843'

def test_no_numbers():
    """test_no_numbers function"""
    site = 'example.org'
    login = 'contact@example.org'
    master_password = 'password'
    password_profile = {'length': 14, 'numbers': False}
    generated_password = generate_password(site, login, master_password, password_profile)
    assert generated_password == 'sB>{qF}wN%/-fm'

def test_no_options():
    """test_no_options function"""
    site = 'example.org'
    login = 'contact@example.org'
    master_password = 'password'
    generated_password = generate_password(site, login, master_password)
    assert generated_password == 'WHLpUL)e00[iHR+w'
