

def ci_test_example():
    """Just a dummy test"""
    assert True


def test_nw():
    import narwhals
    assert narwhals.__version__ == "1.10.0"