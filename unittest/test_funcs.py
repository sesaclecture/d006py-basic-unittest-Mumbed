from funcs import is_odd_even, make_sum, give_max, give_min
def test_odd_even():
    assert True == is_odd_even(2) 
    assert False == is_odd_even(7) 
    assert True == is_odd_even(20) 
    assert True == is_odd_even(0) 


def test_sum():
    assert 15 == make_sum([1,2,3,4,5])
    assert 0 == make_sum([1,2,-3,4,5,-9])


def test_max():
    assert 5 == give_max([1,2,3,4,5])
    assert 8 == give_max([1,2,3,4,5,8])
    assert 165 == give_max([1,2,3,4,5,8,165])

def test_min():
    assert 1 == give_min([1,2,3,4,5])
    assert -6 == give_min([1,2,3,-6,4,5])
    assert 0 == give_min([1,2,3,0,4,5])