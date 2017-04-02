"""lesspass render password unit tests"""

from .lesspass import _get_password_profile
from .lesspass import _render_password
from .lesspass import _insert_string_pseudo_randomly

def test_remainder_as_index():
    """test_remainder_as_index function"""
    entropy = 'dc33d431bce2b01182c613382483ccdb0e2f66482cbba5e9d07dab34acc7eb1e'
    password_profile = _get_password_profile([])
    assert _render_password(entropy, password_profile)[0] == 'W'

def test_quotient_as_second_entropy():
    """test_quotient_as_second_entropy function"""
    entropy = 'dc33d431bce2b01182c613382483ccdb0e2f66482cbba5e9d07dab34acc7eb1e'
    password_profile = _get_password_profile([])
    assert _render_password(entropy, password_profile)[1] == 'H'

def test_default_length_sixteen():
    """test_default_length_sixteen function"""
    entropy = 'dc33d431bce2b01182c613382483ccdb0e2f66482cbba5e9d07dab34acc7eb1e'
    password_profile = _get_password_profile([])
    assert len(_render_password(entropy, password_profile)) == 16

def test_can_specify_length():
    """test_can_specify_length function"""
    entropy = 'dc33d431bce2b01182c613382483ccdb0e2f66482cbba5e9d07dab34acc7eb1e'
    password_profile = _get_password_profile({'length': 20})
    assert len(_render_password(entropy, password_profile)) == 20

def test_one_of_each_set_of_chars():
    """test_one_of_each_set_of_chars function"""
    password = _insert_string_pseudo_randomly('123456', int(7 * 6 + 2), 'uT')
    assert password == 'T12u3456'

def test_at_least_one_of_each_set():
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
    assert len(generated_password) == 6
    assert lowercase_ok and uppercase_ok and numbers_ok and symbols_ok
