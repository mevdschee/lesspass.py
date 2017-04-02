"""lesspass entropy unit tests"""

from .lesspass import _get_password_profile
from .lesspass import _calc_entropy
from .lesspass import _consume_entropy

def test_pbkdf2_with_default_params():
    """test_pbkdf2_with_default_params function"""
    site = 'example.org'
    login = 'contact@example.org'
    master_password = 'password'
    password_profile = _get_password_profile({})
    entropy = _calc_entropy(site, login, master_password, password_profile)
    assert entropy.decode('utf-8') == \
        'dc33d431bce2b01182c613382483ccdb0e2f66482cbba5e9d07dab34acc7eb1e'

def test_with_different_options():
    """test_with_different_options function"""
    site = 'example.org'
    login = 'contact@example.org'
    master_password = 'password'
    password_profile = _get_password_profile({
        'iterations': 8192,
        'keylen': 16,
        'digest': 'sha512'
    })
    entropy = _calc_entropy(site, login, master_password, password_profile)
    assert entropy.decode('utf-8') == 'fff211c16a4e776b3574c6a5c91fd252'

def test_with_counter_one():
    """test_with_counter_one function"""
    site = 'example.org'
    login = 'contact@example.org'
    master_password = 'password'
    password_profile = _get_password_profile({'iterations': 1, 'keylen': 16})
    entropy = _calc_entropy(site, login, master_password, password_profile)
    assert entropy.decode('utf-8') == 'd3ec1e988dd0b3640c7491cd2c2a88b5'

def test_with_counter_two():
    """test_with_counter_two function"""
    site = 'example.org'
    login = 'contact@example.org'
    master_password = 'password'
    password_profile = _get_password_profile({'iterations': 1, 'keylen': 16, 'counter': 2})
    entropy = _calc_entropy(site, login, master_password, password_profile)
    assert entropy.decode('utf-8') == 'ddfb1136260f930c21f6d72f6eddbd40'

def test__consume_entropy():
    """test__consume_entropy function"""
    value, entropy = _consume_entropy('', int(4 * 4 + 2), 'abcd', 2)
    assert value == 'ca'
    assert entropy == 1
