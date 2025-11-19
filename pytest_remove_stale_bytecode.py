import importlib.metadata
import os
import os.path
import sys


__version__ = importlib.metadata.version('pytest-remove-stale-bytecode')
python_version = '{0.major}{0.minor}'.format(sys.version_info)
pytest_version = importlib.metadata.version('pytest')

compiled_suffixes = '.pyc', '.pyo'


def py_path(path):
    path = str(path)[:-1]
    path = path.replace('_PYTEST.py', '.py')
    path = path.replace('-PYTEST.py', '.py')
    path = path.replace('-pytest-{0}.py'.format(pytest_version), '.py')
    path = path.replace('{0}__pycache__{0}'.format(os.path.sep), os.path.sep)
    path = path.replace('.cpython-{}.py'.format(python_version), '.py')
    path = path.replace('.pypy{}.py'.format(python_version), '.py')
    return path


def delete_file(path):
    os.unlink(path)


def pytest_configure(config):
    # When calling pytest with --help `config` has no args:
    for testpath in getattr(config, 'args', []):
        for root, subdirs, files in os.walk(testpath):
            for filename in files:
                path = os.path.join(root, filename)
                if os.path.splitext(path)[1] not in compiled_suffixes:
                    continue
                if os.path.exists(py_path(path)):
                    continue
                if config.getoption('verbose') > 0:
                    print("\nRemoving stale bytecode file %s" % path)
                try:
                    delete_file(path)
                except FileNotFoundError:
                    pass
