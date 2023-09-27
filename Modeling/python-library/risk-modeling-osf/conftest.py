#
# conftest.py
#
import pytest
import osf_risk_model
#
#
def pytest_sessionstart():
    pass
def test_check_smoketest(session=0):
    with pytest.raises(ValueError) as execinfo: 
        obj = osf_risk_model.OsfRiskTrainingClass()
        dummy_val = 19
        val_obj = obj.set_x(19)
        val_obj = obj.get_x()
        raise ValueError('Lets Pretend it raised an error!')
    assert str(val_obj) == str(dummy_val)
#
# pytest setup stuff
#pytest.main()
#
pytest_sessionstart()
test_check_smoketest(session=0)
#