#
# conftest.py
#
import pytest
import osf_risk_training
#
def pytest_sessionstart(session=0, execinfovalue='TEST APP'):
    with pytest.raises(ValueError) as execinfo: 
        obj = osf_risk_training.OsfRiskTrainingClass()
        dummy_val = 20
        val_obj = obj.set_x(19)
    assert str(val_obj) == dummy_val
#    pass
#    return 1
#
# pytest setup stuff
#pytest.main()
#
pytest_sessionstart(session=0, execinfovalue='TEST APP')
#