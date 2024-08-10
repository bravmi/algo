import pytest


def pytest_addoption(parser):
    parser.addoption(
        '--runslow', action='store_true', default=False, help='run slow tests'
    )


def pytest_configure(config):
    config.addinivalue_line('markers', 'slow: mark test as slow to run')


def pytest_collection_modifyitems(config, items):
    if config.getoption('--runslow'):
        # --runslow given in cli: do not skip slow tests
        return
    skip_slow = pytest.mark.skip(reason='need --runslow option to run')
    for item in items:
        if 'slow' in item.keywords:
            item.add_marker(skip_slow)


@pytest.fixture(autouse=True, scope='session')
def set_ipython_config():
    """Set IPython config for pytest ipdb."""
    from _pytest.debugging import pytestPDB

    p = pytestPDB._init_pdb('post_mortem')

    from IPython.terminal import ipapp

    p.shell.config = ipapp.load_default_config()
