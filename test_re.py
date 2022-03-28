import re
import pytest
@pytest.mark.re
def test_areasqr():
    a = 5
    result = re.area_square(a)
    assert result == a*a
@pytest.mark.re
def test_arearec():
    a = 4
    b = 8
    result = re.area_rec(a,b)
    assert result == a*b
@pytest.mark.re
def test_peri():
    a = 78
    b = 8
    result = re.peri_rec(a,b)
    assert result == 2*(a+b)