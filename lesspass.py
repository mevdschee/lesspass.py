"""lesspass implementation in Python"""

import hashlib

CHARACTER_SUBSETS = {
    'lowercase': 'abcdefghijklmnopqrstuvwxyz',
    'uppercase': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
    'numbers': '0123456789',
    'symbols': '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
}

def get_password_profile(password_profile):
    """get_password_profile function"""
    default_password_profile = {
        'lowercase': True,
        'uppercase': True,
        'numbers': True,
        'symbols': True,
        'digest': 'sha256',
        'iterations': 100000,
        'keylen': 32,
        'length': 16,
        'counter': 1,
        'version': 2
    }
    result = default_password_profile.copy()
    if password_profile != None:
        result.update(password_profile)
    return result

def generate_password(site, login, master_password, password_profile=None):
    """generate_password function"""
    password_profile = get_password_profile(password_profile)
    entropy = calc_entropy(site, login, master_password, password_profile)
    return render_password(entropy, password_profile)

def calc_entropy(site, login, master_password, password_profile):
    """calc_entropy function"""
    salt = site + login + hex(password_profile['counter'])[2:]
    return hashlib.pbkdf2_hmac(
        password_profile['digest'],
        master_password,
        salt,
        password_profile['iterations'],
        password_profile['keylen']
    ).encode('hex')

def get_set_of_characters(rules=None):
    """get_set_of_characters function"""
    if rules is None:
        return (
            CHARACTER_SUBSETS['lowercase'] +
            CHARACTER_SUBSETS['uppercase'] +
            CHARACTER_SUBSETS['numbers'] +
            CHARACTER_SUBSETS['symbols']
        )
    set_of_chars = ''
    for rule in rules:
        set_of_chars += CHARACTER_SUBSETS[rule]
    return set_of_chars

def consume_entropy(generated_password, quotient, set_of_characters, max_length):
    """consume_entropy function"""
    if len(generated_password) >= max_length:
        return [generated_password, quotient]
    quotient, remainder = divmod(quotient, len(set_of_characters))
    generated_password += set_of_characters[remainder]
    return consume_entropy(generated_password, quotient, set_of_characters, max_length)

def insert_string_pseudo_randomly(generated_password, entropy, string):
    """insert_string_pseudo_randomly function"""
    for letter in string:
        quotient, remainder = divmod(entropy, len(generated_password))
        generated_password = (
            generated_password[:remainder] +
            letter +
            generated_password[remainder:]
        )
        entropy = quotient
    return generated_password

def get_one_char_per_rule(entropy, rules):
    """get_one_char_per_rule function"""
    one_char_per_rules = ''
    for rule in rules:
        value, entropy = consume_entropy('', entropy, CHARACTER_SUBSETS[rule], 1)
        one_char_per_rules += value
    return [one_char_per_rules, entropy]

def get_configured_rules(password_profile):
    """get_configured_rules function"""
    rules = ['lowercase', 'uppercase', 'numbers', 'symbols']
    return [rule for rule in rules if rule in password_profile and password_profile[rule]]

def render_password(entropy, password_profile):
    """render_password function"""
    rules = get_configured_rules(password_profile)
    set_of_characters = get_set_of_characters(rules)
    password, password_entropy = consume_entropy(
        '',
        long(entropy, 16),
        set_of_characters,
        password_profile['length'] - len(rules)
    )
    characters_to_add, character_entropy = get_one_char_per_rule(password_entropy, rules)
    return insert_string_pseudo_randomly(password, character_entropy, characters_to_add)
