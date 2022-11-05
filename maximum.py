import numbers


def maximum(left: numbers.Real, right: numbers.Real) -> numbers.Real:
    """
    Function:
        maximum
    Inputs:
        left, real number
        right, real number
    Preconditions:
        true
    Output:
        a real number
    Postconditions:
        returns left if left >= right, otherwise returns right
    """
    if left >= right:
        return left
    return right


if __name__ == '__main__':
    assert maximum(left=-1, right=0) == 0
    assert maximum(left=0, right=-1) == 0
    assert maximum(left=-1, right=-1) == -1
    assert maximum(left=0, right=0) == 0
    assert maximum(left=1, right=0) == 1
    assert maximum(left=0, right=1) == 1
    assert maximum(left=1, right=1) == 1
    assert maximum(left=1.1, right=1) == 1.1
    assert maximum(left=1, right=1.1) == 1.1
    assert maximum(left=1.1, right=1.1) == 1.1



