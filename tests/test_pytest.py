# def func(x):
#     return x + 1
#
#
# def test_answer():
#     assert func(3) == 5

# content of test_sysexit.py
# ------------------------------
# import pytest
#
#
# def f():
#     raise SystemExit(1)
#
#
# def test_mytest():
#     with pytest.raises(SystemExit):
#         f()
# ---------------------------------
# content of test_class.py
# class TestClass(object):
#     def test_one(self):
#         x = "this"
#         assert 'h' in x
#
#     def test_two(self):
#         x = "hello"
#         assert hasattr(x, 'check')
a = 10
b = 20
def mul(a, b):
    return a + b