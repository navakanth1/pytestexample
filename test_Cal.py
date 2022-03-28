import Cal


def test_add2no():
    a = 19
    b = 34
    result = Cal.add2no(a,b)
    assert result == a+b
def test_sub2no():
    a = 16
    b = 1414
    result = Cal.sub2no(a,b)
    assert result == a-b
def test_mul2no():
    a = 22
    b = 122
    result = Cal.mul2no(a,b)
    assert result == a*b
def test_div2no():
    a = 23
    b = 12
    result = Cal.div2no(a,b)
    assert result == a/b