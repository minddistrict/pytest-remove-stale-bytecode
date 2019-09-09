import pkg_resources
import os
import os.path
import sys


__version__ = pkg_resources.get_distribution(
    'pytest-remove-stale-bytecode').version
python_version = '{0.major}{0.minor}'.format(sys.version_info)

compiled_suffixes = '.pyc', '.pyo'


def py_path(path):
    path = str(path)[:-1]
    path = path.replace('_PYTEST.py', '.py')
    path = path.replace('-PYTEST.py', '.py')
    path = path.replace('{0}__pycache__{0}'.format(os.path.sep), os.path.sep)
    path = path.replace('.cpython-{}.py'.format(python_version), '.py')
    return path


def pytest_configure(config):
    for testpath in config.args:
        for root, subdirs, files in os.walk(testpath):
            for filename in files:
                path = os.path.join(root, filename)
                if os.path.splitext(path)[1] not in compiled_suffixes:
                    continue
                if os.path.exists(py_path(path)):
                    continue
                if config.getoption('verbose') > 0:
                    print("\nRemoving stale bytecode file %s" % path)
                os.unlink(path)
