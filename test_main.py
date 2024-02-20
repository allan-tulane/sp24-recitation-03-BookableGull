from main import *



## Feel free to add your own tests here.
def test_multiply():
    assert quadratic_multiply(BinaryNumber(3), BinaryNumber(3)) == 3*3
    assert quadratic_multiply(BinaryNumber(1), BinaryNumber(1)) == 1*1
    assert quadratic_multiply(BinaryNumber(999), BinaryNumber(998)) == 999*998
    assert quadratic_multiply(BinaryNumber(8), BinaryNumber(21)) == 8*21
