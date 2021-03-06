
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



def test_gen_lots():
    global cls
    for n in range(1,4):
        assert check_this(n) == True
    for n in range(4, 8):
        assert check_this(n) == False



class report(object):
    def __call__(self, ExpectedResult,desc,value,n):
        self.description = 'Test {}:{}'.format(desc,value)
        assert ExpectedResult == value , '{} {}'.format(ExpectedResult, value)

def test_gen_better_lots():
    global cls
    for n in range(1, 4):
        yield report(), True,  "Test {}".format(n), check_this(n),n
    for n in range(4, 8):
        yield report(), False, "Test {}".format(n), check_this(n),n

def check_this(n):
    global cls
    return cls.isInData(n)