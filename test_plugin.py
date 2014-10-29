pytest_plugins = "pytester",


def test_version():
    import plugin
    assert plugin.__version__
