"""lesspass set of characters unit tests"""

from .lesspass import _get_set_of_characters
from .lesspass import _get_one_char_per_rule
from .lesspass import _get_configured_rules

def test_get_default_characters():
    """test_get_default_characters function"""
    set_of_characters = _get_set_of_characters()
    assert set_of_characters == 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789' + \
        '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    assert len(set_of_characters) == 26 * 2 + 10 + 32

def test_concat_rules_in_order():
    """test_concat_rules_in_order function"""
    set_of_characters = _get_set_of_characters(['lowercase', 'uppercase', 'numbers'])
    assert set_of_characters == 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    assert len(set_of_characters) == 26 * 2 + 10

def test_only_lowercase():
    """test_only_lowercase function"""
    set_of_characters = _get_set_of_characters(['lowercase'])
    assert set_of_characters == 'abcdefghijklmnopqrstuvwxyz'
    assert len(set_of_characters) == 26

def test_only_uppercase():
    """test_only_uppercase function"""
    set_of_characters = _get_set_of_characters(['uppercase'])
    assert set_of_characters == 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    assert len(set_of_characters) == 26

def test_only_numbers():
    """test_only_numbers function"""
    set_of_characters = _get_set_of_characters(['numbers'])
    assert set_of_characters == '0123456789'
    assert len(set_of_characters) == 10

def test_only_symbols():
    """test_only_symbols function"""
    set_of_characters = _get_set_of_characters(['symbols'])
    assert set_of_characters == '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    assert len(set_of_characters) == 32

def test_one_char_per_rule():
    """test_one_char_per_rule function"""
    value, entropy = _get_one_char_per_rule(int(26 * 26), ['lowercase', 'uppercase'])
    assert value == 'aA'
    assert len(value) == 2
    assert entropy == 1

def test_configured_rules():
    """test_configured_rules function"""
    assert _get_configured_rules({'uppercase': True}) == \
        ['uppercase']
    assert _get_configured_rules({'uppercase': True, 'lowercase': True}) == \
        ['lowercase', 'uppercase']
    assert _get_configured_rules({'lowercase': True, 'symbols': False}) == \
        ['lowercase']
    assert _get_configured_rules({'lowercase': True, 'uppercase': True, 'symbols': True, \
        'numbers': True}) == ['lowercase', 'uppercase', 'numbers', 'symbols']
