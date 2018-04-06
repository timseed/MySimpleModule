
from MySimpleModule import MySimpleModule

cls=None

def test_000_init():
    global cls
    cls=MySimpleModule()
    assert cls


def test_010_isin_good():
    global cls
    assert cls.isInData(1) == True


def test_020_isin_bad():
    global cls
    assert cls.isInData(99) == False

def test_030_isin_bad_data():
    global cls
    try:
        cls.isInData("a")
    except Exception as err:
        assert type(err) == ValueError


