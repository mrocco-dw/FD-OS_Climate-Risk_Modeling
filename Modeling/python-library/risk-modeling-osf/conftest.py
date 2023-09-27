#
# conftest.py
#
import pytest
import osf_risk_training
#
def pytest_sessionstart(session=0, execinfovalue='TEST APP'):
    with pytest.raises(ValueError) as execinfo: 
        obj = osf_risk_training.OsfRiskTrainingClass()
        dummy_val = 19
        val_obj = obj.set_x(19)
        val_obj = obj.get_x()
        raise ValueError('Lets Pretend it raised an error!')
    assert str(val_obj) == dummy_val
#
# pytest setup stuff
#pytest.main()
#
pytest_sessionstart(session=0, execinfovalue='TEST APP')
#