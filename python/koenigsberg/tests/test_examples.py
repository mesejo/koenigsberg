

def ci_test_example():
    """Just a dummy test"""
    assert True


def test_nw():
    import narwhals
    assert narwhals.__version__ is not None


def test_foo():
    """Just another dummy test"""
    assert True