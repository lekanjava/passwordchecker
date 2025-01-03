from passwordstrength.main import check_password_strength

def test_password_strength():
    assert check_password_strength("12345678") == 2
    assert check_password_strength("Password123!") == 5
    assert check_password_strength("weak") == 1
