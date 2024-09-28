from bank import value

def main():
    test_return_zero()
    test_return_20()

def test_return_zero():
    assert value('hello gi') == 0
    assert value('Hello') == 0
    assert value('Hello Gi') == 0

def test_return_20():
    assert value('Hi') == 20
    assert value('hey') == 20

def test_return_100():
    assert value("What's up?") == 100
    assert value("good morning") == 100 

