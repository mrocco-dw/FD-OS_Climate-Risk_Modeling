#
# conftest.py
#
import pytest
import osf_model_app
#
def pytest_sessionstart():
    pass
def test_check_smoketest(session=0, execinfovalue='TEST APP'):
    with pytest.raises(ValueError) as execinfo:
        execinfovalue = execinfovalue
        app = osf_model_app.OsfModel.webapp(assets_dir='', model_name='')
        raise ValueError('Lets Pretend it raised an error!')
    assert str(execinfovalue) == str('TEST APP')
#
# pytest setup stuff
# pytest.main()
#
pytest_sessionstart()
test_check_smoketest(session=0, execinfovalue='TEST APP')
#