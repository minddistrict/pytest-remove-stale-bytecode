import pkg_resources
import os.path


__version__ = pkg_resources.get_distribution(
    'pytest-remove-stale-bytecode').version

compiled_suffixes = '.pyc', '.pyo'


def pytest_collect_file(path, parent):
    if path.ext not in compiled_suffixes:
        return
    if path.fnmatch('*PYTEST.py[co]'):
        return
    if os.path.exists(str(path)[:-1]):
        return
    print("\nRemoving stale bytecode file %s" % path)
    path.remove()
