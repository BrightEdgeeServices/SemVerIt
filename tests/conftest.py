"""Create a conftest.py

Define the fixture functions in this file to make them accessible across multiple test files.
"""


from pathlib import Path
import pytest
from beetools.beearchiver import Archiver
from beetools.beeutils import rm_tree


_PROJ_DESC = __doc__.split("\n")[0]
_PROJ_PATH = Path(__file__)
_PROJ_NAME = _PROJ_PATH.stem
_PROJ_VERSION = "0.0.1"


b_tls = Archiver(_PROJ_NAME, _PROJ_VERSION, _PROJ_DESC, _PROJ_PATH)

_setup_py_contents = """import setuptools

setuptools.setup(
    name="SemVerIt",
    version="2.3.4",
    author="Hendrik du Toit",
    author_email="hendrik@brightedge.co.za",
    description="Project description",
    long_description="Project long description",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Topic :: Software Development",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
    ],
)
"""


@pytest.fixture
def setup_env(tmp_path):
    """Setup the environment base structure"""
    working_dir = tmp_path
    yield working_dir
    rm_tree(working_dir)


@pytest.fixture
def create_setup_py(setup_env):
    working_dir = setup_env
    setup_py_pth = working_dir / "setup.py"
    setup_py_pth.write_text(_setup_py_contents)
    return setup_py_pth


del b_tls
