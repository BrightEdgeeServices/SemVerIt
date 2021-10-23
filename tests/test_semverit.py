"""Testing semverit__init__()"""

from pathlib import Path
from beetools.beearchiver import Archiver
import semverit


_PROJ_DESC = __doc__.split("\n")[0]
_PROJ_PATH = Path(__file__)
_PROJ_NAME = _PROJ_PATH.stem
_PROJ_VERSION = "0.0.1"


b_tls = Archiver(_PROJ_NAME, _PROJ_VERSION, _PROJ_DESC, _PROJ_PATH)


class TestSemVerIt:
    def test__init__default(self):
        """Assert class __init__"""
        t_semverit = semverit.SemVerIt()
        assert t_semverit.success
        assert t_semverit.maj == 0
        assert t_semverit.min == 0
        assert t_semverit.patch == 1
        assert t_semverit.version == "0.0.1"
        pass

    def test__init__set_version(self):
        """Assert class __init__"""
        t_semverit = semverit.SemVerIt(p_version="3.2.1")
        assert t_semverit.success
        assert t_semverit.maj == 3
        assert t_semverit.min == 2
        assert t_semverit.patch == 1
        assert t_semverit.version == "3.2.1"
        pass

    def test__init__setup_py(self, create_setup_py):
        """Assert class __init__"""
        setup_pth = create_setup_py
        t_semverit = semverit.SemVerIt(p_setup_py_pth=setup_pth)
        assert t_semverit.success
        assert t_semverit.maj == 2
        assert t_semverit.min == 3
        assert t_semverit.patch == 4
        assert t_semverit.version == "2.3.4"
        pass

    def test_bump_maj(self, setup_env):
        """Assert class __init__"""
        t_semverit = semverit.SemVerIt()
        assert t_semverit.bump_maj() == "1.0.0"
        pass

    def test_bump_min(self, setup_env):
        """Assert class __init__"""
        t_semverit = semverit.SemVerIt()
        assert t_semverit.bump_min() == "0.1.0"
        pass

    def test_bump_patch(self, setup_env):
        """Assert class __init__"""
        t_semverit = semverit.SemVerIt()
        assert t_semverit.bump_patch() == "0.0.2"
        pass

    def test_get_from_setup_py(self, create_setup_py):
        """Assert class __init__"""
        setup_pth = create_setup_py
        t_semverit = semverit.SemVerIt()
        t_semverit.get_from_setup_py(setup_pth)
        assert t_semverit.version == "2.3.4"
        pass

    def test_do_examples(self, create_setup_py):
        """Assert class __init__"""
        semverit.do_examples()


del b_tls
