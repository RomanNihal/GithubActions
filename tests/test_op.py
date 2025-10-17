from src.math_op import add, sub

def test_add():
    assert add(2,3)==5
    assert add(7,5)==12
    assert add(-5,6)==1

def test_sub():
    assert sub(5,3)==2
    assert sub(-2,2)==-4
    assert sub(5,-3)==8