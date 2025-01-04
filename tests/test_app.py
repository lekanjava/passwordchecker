from passwordstrength.main import check_password_strength

def test_password_strength():
    # Test weak passwords
    assert check_password_strength("12345678", return_numeric=True) == 1
    assert check_password_strength("weak", return_numeric=True) == 1
    assert check_password_strength("password", return_numeric=True) == 1

    # Test moderate passwords
    assert check_password_strength("Password123", return_numeric=True) == 2
    assert check_password_strength("1234abcd", return_numeric=True) == 2

    # Test strong passwords
    assert check_password_strength("Password123!", return_numeric=True) == 3
    assert check_password_strength("Str0ngP@ssw0rd!", return_numeric=True) == 3
