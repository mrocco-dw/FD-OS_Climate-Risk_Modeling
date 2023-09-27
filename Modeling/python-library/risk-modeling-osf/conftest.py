#
# conftest.py
#
import pytest
import osf_risk_training
#
def pytest_sessionstart(session=0, execinfovalue='TEST APP'):
    with pytest.raises(ValueError) as execinfo: 
        obj = osf_risk_training.OsfRiskTrainingClass()
        val = []
        dummy = []
        dummy.val = 20
        val.obj = obj.set_x(19)
    assert str(val.obj) == dummy.val
#    pass
#    return 1
#
# pytest setup stuff
#pytest.main()
#
pytest_sessionstart(session=0, execinfovalue='TEST APP')
#