"""Create a conftest.py

Define the fixture functions in this file to make them accessible across multiple test files.
"""


from pathlib import Path
import pytest
from beetools.beearchiver import Archiver
from beetools.beeutils import rm_tree

_PROJ_DESC = __doc__.split("\n")[0]
_PROJ_PATH = Path(__file__)

b_tls = Archiver(_PROJ_DESC, _PROJ_PATH)

_setup_cfg_contents = """\
[metadata]
    version = 2.3.4
"""

_setup_cfg_contents_faulty = """\
[metadata]
    something = 2.3.4
"""


@pytest.fixture
def setup_env(tmp_path):
    """Setup the environment base structure"""
    working_dir = tmp_path
    yield working_dir
    rm_tree(working_dir)


@pytest.fixture
def create_setup_cfg(setup_env):
    working_dir = setup_env
    setup_py_pth = working_dir / "setup.cfg"
    setup_py_pth.write_text(_setup_cfg_contents)
    return setup_py_pth


@pytest.fixture
def create_setup_cfg_faulty(setup_env):
    working_dir = setup_env
    setup_py_pth = working_dir / "setup.cfg"
    setup_py_pth.write_text(_setup_cfg_contents_faulty)
    return setup_py_pth


@pytest.fixture
def sample_set():
    return [
        "4.0.0",
        "4.6.4",
        "4.4.6",
        "5.4.5",
        "5.5.4",
        "5.5.5",
        "5.5.6",
        "5.6.5",
        "6.0.0",
        "6.4.6",
        "6.6.4",
    ]


del b_tls
