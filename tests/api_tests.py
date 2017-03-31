"""lesspass api unit tests"""

import lesspass

def test_render_password():
    """test_render_password function"""
    site = 'example.org'
    login = 'contact@example.org'
    master_password = 'password'
    password_profile = []
    generated_password = lesspass.generate_password(site, login, master_password, password_profile)
    assert generated_password == 'WHLpUL)e00[iHR+w'
