import pkg_resources


__version__ = pkg_resources.get_distribution(
    'pytest-remove-stale-bytecode').version
