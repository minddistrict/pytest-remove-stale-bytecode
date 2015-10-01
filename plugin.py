import pkg_resources
import os.path
import sys


__version__ = pkg_resources.get_distribution(
    'pytest-remove-stale-bytecode').version
python_version = '{0.major}{0.minor}'.format(sys.version_info)

compiled_suffixes = '.pyc', '.pyo'


def py_path(path):
    path = str(path)[:-1]
    path = path.replace('_PYTEST.py', '.py')
    path = path.replace('{0}__pycache__{0}'.format(os.path.sep), os.path.sep)
    path = path.replace('.cpython-{}.py'.format(python_version), '.py')
    return path


def pytest_collect_file(path, parent):
    if path.ext not in compiled_suffixes:
        return
    if os.path.exists(py_path(path)):
        return
    print("\nRemoving stale bytecode file %s" % path)
    path.remove()
