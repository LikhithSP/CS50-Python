from project import is_valid, month_to_integer
import pytest


def test_is_valid():
    assert is_valid("October 20, 2000") == ('October', '20', '2000')
    assert is_valid("nov 02,2001") == ('nov', '02', '2001')


def test_is_valid_valueerror():
    with pytest.raises(ValueError):
        is_valid("October 20 2000")
    with pytest.raises(ValueError):
        is_valid("Septembers 05, 2003")
    with pytest.raises(ValueError):
        is_valid("jan 34, 2005")
    with pytest.raises(ValueError):
        is_valid("Feb 11, 200")


def test_month_to_integer():
    assert month_to_integer("oct") == 10
    assert month_to_integer("november") == 11


def test_month_to_integer_valueerror():
    with pytest.raises(ValueError):
        month_to_integer('Septembers')
    with pytest.raises(ValueError):
        month_to_integer('febraury')
