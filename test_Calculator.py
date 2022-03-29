import Calculator
import pytest
@pytest.mark.parametrize("a,b,c",[(5,2,7),(8,2,10),(1,2,3),(2,3,5)])
def test_add2no(a,b,c):

    res=Calculator.add2no(a,b)
    assert res == c
@pytest.mark.parametrize("a,b,c",[(5,2,7),(8,2,10),(1,2,3),(4,3,7)])
def test_sub2no(a,b,c):

    res=Calculator.sub2no(a,b)
    assert res == c
@pytest.mark.parametrize("a,b,c",[(5,2,7),(8,2,10),(1,2,3),(4,3,7)])
def test_mul2no(a,b,c):

    res=Calculator.mul2no(a,b)
    assert res == c
@pytest.mark.parametrize("a,b,c",[(6,2,8),(8,2,10),(6,2,8),(18,3,21)])
@pytest.mark.muldiv
def test_div2no(a,b,c):

    res=Calculator.div2no(a,b)
    assert res ==c