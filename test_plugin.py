import pytest
from plugin import python_version

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

    result = testdir.runpytest()

    assert not any(
        line.startswith("Removing stale bytecode file")
        for line in result.outlines)
    assert not bar.exists()
    assert fooco.exists()
    assert foo.exists()


@pytest.mark.parametrize("ext", ['pyc', 'pyo'])
def test_plugin_removes_bytecode_files_verbosely(testdir, ext):
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
def test_plugin_removes_PYTEST_bytecode_files(testdir, ext):
    foo = testdir.makefile('py', foo='')
    foopytest = testdir.makefile(ext, foo_PYTEST='')
    bar = testdir.makefile(ext, bar_PYTEST='')
    testdir.runpytest("-v")
    assert foo.exists()
    assert foopytest.exists()
    assert not bar.exists()


@pytest.mark.parametrize("ext", ['pyc', 'pyo'])
def test_plugin_removes_python3_bytecode_files(testdir, ext):
    foo = testdir.makefile('py', foo='')
    pycache = testdir.mkdir('__pycache__')
    fooco_name = 'foo.cpython-{}.{}'.format(python_version, ext)
    fooco = pycache.ensure(fooco_name)
    barco_name = 'bar.cpython-{}.{}'.format(python_version, ext)
    barco = pycache.ensure(barco_name)
    testdir.runpytest("-v")
    assert foo.exists()
    assert fooco.exists()
    assert not barco.exists()


@pytest.mark.parametrize("ext", ['pyc', 'pyo'])
def test_plugin_removes_python3_PYTEST_bytecode_files(testdir, ext):
    foo = testdir.makefile('py', foo='')
    pycache = testdir.mkdir('__pycache__')
    fooco_name = 'foo.cpython-{}-PYTEST.{}'.format(python_version, ext)
    fooco = pycache.ensure(fooco_name)
    barco_name = 'bar.cpython-{}-PYTEST.{}'.format(python_version, ext)
    barco = pycache.ensure(barco_name)
    testdir.runpytest("-v")
    assert foo.exists()
    assert fooco.exists()
    assert not barco.exists()


def test_plugin_does_not_break_if_file_is_removed_externally(testdir):
    bar = testdir.makefile('pyc', bar='')
    with mock.patch('plugin.delete_file', side_effect=OSError):
        testdir.runpytest("-v")
    assert bar.exists()
