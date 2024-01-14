import pytest

from src.main import Foo, bar, CustomError


@pytest.fixture
def foo():
    '''Returns a bar of 20'''
    return Foo(20)

def test_bar_is_bar():
    '''Returns a bar'''
    assert bar() == "bar"

def test_foo(foo):
    '''Returns value of foo'''
    assert foo.value == 20

def test_foo_raise_error(foo):
    with pytest.raises(CustomError):
        foo.bar()
