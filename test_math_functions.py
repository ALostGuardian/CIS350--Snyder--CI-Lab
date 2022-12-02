from math_functions import *
def test_calc_addition():
 output = add_numbers(2,4)
 assert output == 6
def test_calc_substraction():
 output = subtract_numbers(2, 4)
 assert output == -2
def test_calc_multiply():
 output = multiply_numbers(2,4)
 assert output == 8
def test_calc_multiply_fail():
 output = multiply_numbers(2,4)
 assert output == 8
def test_calc_divide():
 output = divide_numbers(10,2)
 assert output == 5
def test_square_root():
    output = square_root(16)
    assert output == 4
def test_multi_delete():
    output = multi_delete(5,2,3)
    assert output == 0


