import Cal


def test_add2no():
    a = 10
    b = 20
    result = Cal.add2no(a,b)
    assert result == a+b
def test_sub2no():
    a = 15
    b = 14
    result = Cal.sub2no(a,b)
    assert result == a-b
def test_mul2no():
    a = 54
    b = 71
    result = Cal.mul2no(a,b)
    assert result == a*b
def test_div2no():
    a = 45
    b = 10
    result = Cal.div2no(a,b)
    assert result == a/b