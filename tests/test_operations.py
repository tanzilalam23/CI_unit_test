from src.math_operations import add, sub

def test_add():
    assert add(2,3)==5 
    assert add(-4,5)==1
    assert add(9,1)==10

def test_sub():
    assert sub(2,3)==-1
    assert sub(-4,5)==-9
    assert sub(9,1)==8