"""Testing semverit__init__()"""

from pathlib import Path
from beetools.beearchiver import Archiver
import semverit


_PROJ_DESC = __doc__.split("\n")[0]
_PROJ_PATH = Path(__file__)
_PROJ_NAME = _PROJ_PATH.stem


b_tls = Archiver(_PROJ_DESC, _PROJ_PATH)


class TestSemVerIt:
    def test__init__default(self):
        """Assert class __init__"""
        t_semverit = semverit.SemVerIt()
        assert t_semverit.success
        assert t_semverit.maj == 1
        assert t_semverit.min == 0
        assert t_semverit.patch == 0
        assert t_semverit.version == "0.0.0"

    def test__init__logging(self):
        """Assert class __init__"""
        t_semverit = semverit.SemVerIt(p_parent_log_name=_PROJ_NAME)
        assert t_semverit.success
        assert t_semverit.maj == 0
        assert t_semverit.min == 0
        assert t_semverit.patch == 0
        assert t_semverit.version == "0.0.0"
        assert t_semverit._log_name == "{}.semverit".format(_PROJ_NAME)
        assert t_semverit.logger
        assert t_semverit.logger

    def test__init__version_str(self):
        """Assert class __init__"""
        t_semverit = semverit.SemVerIt(p_version="3.2.1")
        assert t_semverit.success
        assert t_semverit.maj == 3
        assert t_semverit.min == 2
        assert t_semverit.patch == 1
        assert t_semverit.version == "3.2.1"

    def test__init__setup_cfg(self, create_setup_cfg):
        """Assert class __init__"""
        setup_pth = create_setup_cfg
        t_semverit = semverit.SemVerIt(p_version=setup_pth)
        assert t_semverit.success
        assert t_semverit.maj == 2
        assert t_semverit.min == 3
        assert t_semverit.patch == 4
        assert t_semverit.version == "2.3.4"

    def test__init__version_list_int(self):
        """Assert class __init__"""
        t_semverit = semverit.SemVerIt(p_version=[3, 2, 1])
        assert t_semverit.success
        assert t_semverit.maj == 3
        assert t_semverit.min == 2
        assert t_semverit.patch == 1
        assert t_semverit.version == "3.2.1"

    def test__init__version_list_str(self):
        """Assert class __init__"""
        t_semverit = semverit.SemVerIt(p_version=["3", "2", "1"])
        assert t_semverit.success
        assert t_semverit.maj == 3
        assert t_semverit.min == 2
        assert t_semverit.patch == 1
        assert t_semverit.version == "3.2.1"

    def test__eq__default(self, sample_set):
        """Assert class __init__"""
        t_semverit = semverit.SemVerIt("5.5.5")
        t_semverit = semverit.SemVerIt("5.5.5")
        assert not t_semverit == sample_set[0]  # '4.0.0'
        assert not t_semverit == semverit.SemVerIt(sample_set[0])

        assert not t_semverit == sample_set[1]  # '4.6.4'
        assert not t_semverit == semverit.SemVerIt(sample_set[1])

        assert not t_semverit == sample_set[2]  # '4.4.6'
        assert not t_semverit == semverit.SemVerIt(sample_set[2])

        assert not t_semverit == sample_set[3]  # '5.4.5'
        assert not t_semverit == semverit.SemVerIt(sample_set[3])

        assert not t_semverit == sample_set[4]  # '5.5.4'
        assert not t_semverit == semverit.SemVerIt(sample_set[4])

        assert t_semverit == sample_set[5]  # '5.5.5'
        assert t_semverit == semverit.SemVerIt(sample_set[5])

        assert not t_semverit == sample_set[6]  # '5.5.6'
        assert not t_semverit == semverit.SemVerIt(sample_set[6])

        assert not t_semverit == sample_set[7]  # '5.6.5'
        assert not t_semverit == semverit.SemVerIt(sample_set[7])

        assert not t_semverit == sample_set[8]  # '6.0.0'
        assert not t_semverit == semverit.SemVerIt(sample_set[8])

        assert not t_semverit == sample_set[9]  # '6.4.6'
        assert not t_semverit == semverit.SemVerIt(sample_set[9])

        assert not t_semverit == sample_set[10]  # '6.6.4'
        assert not t_semverit == semverit.SemVerIt(sample_set[10])

    def test__le__default(self, sample_set):
        """Assert class __init__"""
        t_semverit = semverit.SemVerIt("5.5.5")
        assert not t_semverit <= sample_set[0]  # '4.0.0'
        assert not t_semverit <= semverit.SemVerIt(sample_set[0])

        assert not t_semverit <= sample_set[1]  # '4.6.4'
        assert not t_semverit <= semverit.SemVerIt(sample_set[1])

        assert not t_semverit <= sample_set[2]  # '4.4.6'
        assert not t_semverit <= semverit.SemVerIt(sample_set[2])

        assert not t_semverit <= sample_set[3]  # '5.4.5'
        assert not t_semverit <= semverit.SemVerIt(sample_set[3])

        assert not t_semverit <= sample_set[4]  # '5.5.4'
        assert not t_semverit <= semverit.SemVerIt(sample_set[4])

        assert t_semverit <= sample_set[5]  # '5.5.5'
        assert t_semverit <= semverit.SemVerIt(sample_set[5])

        assert t_semverit <= sample_set[6]  # '5.5.6'
        assert t_semverit <= semverit.SemVerIt(sample_set[6])

        assert t_semverit <= sample_set[7]  # '5.6.5'
        assert t_semverit <= semverit.SemVerIt(sample_set[7])

        assert t_semverit <= sample_set[8]  # '6.0.0'
        assert t_semverit <= semverit.SemVerIt(sample_set[8])

        assert t_semverit <= sample_set[9]  # '6.4.6'
        assert t_semverit <= semverit.SemVerIt(sample_set[9])

        assert t_semverit <= sample_set[10]  # '6.6.4'
        assert t_semverit <= semverit.SemVerIt(sample_set[10])

        assert not t_semverit <= 0.0  # 0.0 Float

    def test__lt__default(self, sample_set):
        """Assert class __init__"""
        t_semverit = semverit.SemVerIt("5.5.5")
        assert not t_semverit < sample_set[0]  # '4.0.0'
        assert not t_semverit < semverit.SemVerIt(sample_set[0])

        assert not t_semverit < sample_set[1]  # '4.6.4'
        assert not t_semverit < semverit.SemVerIt(sample_set[1])

        assert not t_semverit < sample_set[2]  # '4.4.6'
        assert not t_semverit < semverit.SemVerIt(sample_set[2])

        assert not t_semverit < sample_set[3]  # '5.4.5'
        assert not t_semverit < semverit.SemVerIt(sample_set[3])

        assert not t_semverit < sample_set[4]  # '5.5.4'
        assert not t_semverit < semverit.SemVerIt(sample_set[4])

        assert not t_semverit < sample_set[5]  # '5.5.5'
        assert not t_semverit < semverit.SemVerIt(sample_set[5])

        assert t_semverit < sample_set[6]  # '5.5.6'
        assert t_semverit < semverit.SemVerIt(sample_set[6])

        assert t_semverit < sample_set[7]  # '5.6.5'
        assert t_semverit < semverit.SemVerIt(sample_set[7])

        assert t_semverit < sample_set[8]  # '6.0.0'
        assert t_semverit < semverit.SemVerIt(sample_set[8])

        assert t_semverit < sample_set[9]  # '6.4.6'
        assert t_semverit < semverit.SemVerIt(sample_set[9])

        assert t_semverit < sample_set[10]  # '6.6.4'
        assert t_semverit < semverit.SemVerIt(sample_set[10])

        assert not t_semverit < 0.0  # 0.0 Float

    def test__ge__default(self, sample_set):
        """Assert class __init__"""
        t_semverit = semverit.SemVerIt("5.5.5")
        assert t_semverit >= sample_set[0]  # '4.0.0'
        assert t_semverit >= semverit.SemVerIt(sample_set[0])

        assert t_semverit >= sample_set[1]  # '4.6.4'
        assert t_semverit >= semverit.SemVerIt(sample_set[1])

        assert t_semverit >= sample_set[2]  # '4.4.6'
        assert t_semverit >= semverit.SemVerIt(sample_set[2])

        assert t_semverit >= sample_set[3]  # '5.4.5'
        assert t_semverit >= semverit.SemVerIt(sample_set[3])

        assert t_semverit >= sample_set[4]  # '5.5.4'
        assert t_semverit >= semverit.SemVerIt(sample_set[4])

        assert t_semverit >= sample_set[5]  # '5.5.5'
        assert t_semverit >= semverit.SemVerIt(sample_set[5])

        assert not t_semverit >= sample_set[6]  # '5.5.6'
        assert not t_semverit >= semverit.SemVerIt(sample_set[6])

        assert not t_semverit >= sample_set[7]  # '5.6.5'
        assert not t_semverit >= semverit.SemVerIt(sample_set[7])

        assert not t_semverit >= sample_set[8]  # '6.0.0'
        assert not t_semverit >= semverit.SemVerIt(sample_set[8])

        assert not t_semverit >= sample_set[9]  # '6.4.6'
        assert not t_semverit >= semverit.SemVerIt(sample_set[9])

        assert not t_semverit >= sample_set[10]  # '6.6.4'
        assert not t_semverit >= semverit.SemVerIt(sample_set[10])

        assert not t_semverit >= 0.0  # 0.0 Float

    def test__gt__default(self, sample_set):
        """Assert class __init__"""
        t_semverit = semverit.SemVerIt("5.5.5")
        assert t_semverit > sample_set[0]  # '4.0.0'
        assert t_semverit > semverit.SemVerIt(sample_set[0])

        assert t_semverit > sample_set[1]  # '4.6.4'
        assert t_semverit > semverit.SemVerIt(sample_set[1])

        assert t_semverit > sample_set[2]  # '4.4.6'
        assert t_semverit > semverit.SemVerIt(sample_set[2])

        assert t_semverit > sample_set[3]  # '5.4.5'
        assert t_semverit > semverit.SemVerIt(sample_set[3])

        assert t_semverit > sample_set[4]  # '5.5.4'
        assert t_semverit > semverit.SemVerIt(sample_set[4])

        assert not t_semverit > sample_set[5]  # '5.5.5'
        assert not t_semverit > semverit.SemVerIt(sample_set[5])

        assert not t_semverit > sample_set[6]  # '5.5.6'
        assert not t_semverit > semverit.SemVerIt(sample_set[6])

        assert not t_semverit > sample_set[7]  # '5.6.5'
        assert not t_semverit > semverit.SemVerIt(sample_set[7])

        assert not t_semverit > sample_set[8]  # '6.0.0'
        assert not t_semverit > semverit.SemVerIt(sample_set[8])

        assert not t_semverit > sample_set[9]  # '6.4.6'
        assert not t_semverit > semverit.SemVerIt(sample_set[9])

        assert not t_semverit > sample_set[10]  # '6.6.4'
        assert not t_semverit > semverit.SemVerIt(sample_set[10])

        assert not t_semverit > 0.0  # 0.0 Float

    def test__ne__default(self, sample_set):
        """Assert class __init__"""
        t_semverit = semverit.SemVerIt("5.5.5")
        assert t_semverit != sample_set[0]  # '4.0.0'
        assert t_semverit != semverit.SemVerIt(sample_set[0])

        assert t_semverit != sample_set[1]  # '4.6.4'
        assert t_semverit != semverit.SemVerIt(sample_set[1])

        assert t_semverit != sample_set[2]  # '4.4.6'
        assert t_semverit != semverit.SemVerIt(sample_set[2])

        assert t_semverit != sample_set[3]  # '5.4.5'
        assert t_semverit != semverit.SemVerIt(sample_set[3])

        assert t_semverit != sample_set[4]  # '5.5.4'
        assert t_semverit != semverit.SemVerIt(sample_set[4])

        assert not t_semverit != sample_set[5]  # '5.5.5'
        assert not t_semverit != semverit.SemVerIt(sample_set[5])

        assert t_semverit != sample_set[6]  # '5.5.6'
        assert t_semverit != semverit.SemVerIt(sample_set[6])

        assert t_semverit != sample_set[7]  # '5.6.5'
        assert t_semverit != semverit.SemVerIt(sample_set[7])

        assert t_semverit != sample_set[8]  # '6.0.0'
        assert t_semverit != semverit.SemVerIt(sample_set[8])

        assert t_semverit != sample_set[9]  # '6.4.6'
        assert t_semverit != semverit.SemVerIt(sample_set[9])

        assert t_semverit != sample_set[10]  # '6.6.4'
        assert t_semverit != semverit.SemVerIt(sample_set[10])

        assert not t_semverit != 0.0  # 0.0 Float

        pass

    def test__repr__default(self, sample_set):
        """Assert class __init__"""
        t_semverit = semverit.SemVerIt("5.5.5")
        assert t_semverit == "5.5.5"
        pass

    def test__str__default(self, sample_set):
        """Assert class __init__"""
        t_semverit = semverit.SemVerIt("5.5.5")
        assert t_semverit == "5.5.5"
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
        assert t_semverit.bump_patch() == "0.0.1"
        pass

    def test_get_from_setup_cfg(self, create_setup_cfg):
        """Assert class __init__"""
        setup_pth = create_setup_cfg
        t_semverit = semverit.SemVerIt()
        t_semverit.get_from_setup_cfg(setup_pth)
        assert t_semverit.version == "2.3.4"
        pass

    def test_get_from_setup_cfg_with_no_version(self, create_setup_cfg_faulty):
        """Assert class __init__"""
        setup_pth = create_setup_cfg_faulty
        t_semverit = semverit.SemVerIt()
        t_semverit.get_from_setup_cfg(setup_pth)
        assert t_semverit.version == "0.0.0"
        pass

    def test_do_examples(self):
        """Assert class __init__"""
        semverit.do_examples()


del b_tls
