import pytest
from calc.calc import Calc

def test_add_two_numbers():
    c = Calc()
    res = c.add(4,5)
    assert res == 9

def test_add_three_numbers():
    c = Calc()
    res = c.add(4,5,6)
    assert res == 15

def test_add_too_many_arguments():
    # array of numbers from 0 to 99
    s = range(100)
    c = Calc()
    res = c.add(*s)
    assert res == 4950

def test_subtract_two_numbers():
    c = Calc()
    res = c.sub(10, 3)
    assert res == 7

def test_multiple_two_numbers():
    c = Calc()
    res = c.mult(4, 2)
    assert res == 8

def test_multiple_six_numbers():
    c = Calc()
    res = c.mult(4, 2, 3, 5, 8, 6)
    assert res == 5760

def test_multiple_too_many_numbers():
    m = range(1, 10)
    c = Calc()
    res = c.mult(*m)
    assert res == 362880

def test_div_two_numbers():
    c = Calc()
    res = c.div(13, 2)
    assert res == 6.5

def test_div_by_zero_return_inf():
    c = Calc()
    res = c.div(13, 0)
    assert res == 'inf'

def test_div_zero_by_number():
    c = Calc()
    res = c.div(0, 13)
    assert res == 0

def test_mul_by_zero_raises_exception():
    c = Calc()

    with pytest.raises(ValueError):
        c.mult(0, 3, 8, 9)
    
def test_avg_correct_average():
    c = Calc()
    res = c.avg([2,5,12,98])
    assert res == 29.25

def test_avg_removes_upper_outliers():
    c = Calc()

    res = c.avg([2,5,12,98], ut=90)
    assert res == pytest.approx(6.33333)

def test_avg_removes_lower_outliers():
    c = Calc()

    res = c.avg([2,5,12,98], lt=10)
    assert res == pytest.approx(55)

def test_avg_upper_threshold_is_included():
    c = Calc()

    res = c.avg([2,5,12,98], ut=98)
    assert res == 29.25

def test_avg_lower_threshold_is_included():
    c = Calc()

    res = c.avg([2,5,12,98], lt=2)
    assert res == 29.25

def test_avg_empty_list():
    c = Calc()

    res = c.avg([])
    assert res == 0

def test_avg_manages_empty_list_after_outlier_remove():
    c = Calc()
    res = c.avg([12, 98], lt=15, ut=90)
    assert res == 0

def test_avg_manages_empty_list_before_outlier_removal():
    c = Calc()
    res = c.avg([], lt=15, ut=90)
    assert res == 0

def test_avg_manages_zero_value_lower_outlier():
    c = Calc()
    res = c.avg([-1,0,1], lt=0)
    assert res == 0.5

def test_avg_manages_zero_value_upper_outlier():
    c = Calc()
    res = c.avg([-1,0,1], ut=0)
    assert res == -0.5