def valid_password_full(password: str) -> bool:
    """
    Function:
        valid_password_full
    Inputs:
        password, a string
    Preconditions:
        true
    Output:
        returns a Boolean
    Postconditions:
        returns true if and only if password contains a digit and a lowercase letter
    """
    has_digit = False
    has_lowercase = False
    for char in password:
        if char >= 0 and char <= 9:
            has_digit = True
        if char >= "a" and char <= "z":
            has_lowercase = True
    return has_digit and has_lowercase

def valid_password(password: str) -> bool:
    """
    Function:
        valid_password
    Inputs:
        password, a string
    Preconditions:
        true
    Output:
        returns a Boolean
    Postconditions:
        returns true if and only if password contains a digit and a lowercase letter
    """
    has_digit = False
    has_lowercase = False
    for char in password:
        if char >= 0 and char <= 9:
            has_digit = True
        if char >= "a" and char <= "z":
            has_lowercase = True
        if has_digit and has_lowercase:
            return True
    return False


if __name__ == '__main__':
    assert valid_password_full(password="ABCD3F") == False
    assert valid_password_full(password="ABCDEf") == False
    assert valid_password_full(password="ABCDEF") == False
    assert valid_password_full(password="ABCD3f") == True
    assert valid_password(password="ABCD3F") == False
    assert valid_password(password="ABCDEf") == False
    assert valid_password(password="ABCDEF") == False
    assert valid_password(password="ABCD3f") == True
