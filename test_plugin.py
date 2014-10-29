import pytest

pytest_plugins = "pytester",


def test_version():
    import plugin
    assert plugin.__version__


@pytest.mark.parametrize("ext", ['pyc', 'pyo'])
def test_plugin_removes_bytecode_files(testdir, ext):
    foo = testdir.makefile('py', foo='')
    fooco = testdir.makefile(ext, foo='')
    bar = testdir.makefile(ext, bar='')

    assert len(testdir.tmpdir.listdir()) == 3

    result = testdir.runpytest("-v")

    result.stdout.fnmatch_lines([
        "Removing stale bytecode file *bar.{}".format(ext),
    ])
    assert not bar.exists()
    assert fooco.exists()
    assert foo.exists()


@pytest.mark.parametrize("ext", ['pyc', 'pyo'])
def test_plugin_ignores_PYTEST_bytecode_files(testdir, ext):
    foo = testdir.makefile(ext, foo_PYTEST='')
    testdir.runpytest("-v")
    assert foo.exists()
