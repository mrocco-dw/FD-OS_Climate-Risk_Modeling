#
# conftest.py
#
import pytest
import osf_model_app
#
def pytest_sessionstart(session=0, execinfovalue='TEST APP'):
    with pytest.raises(ValueError) as execinfo:
        execinfovalue = 'TEST APP'
        raise ValueError('Lets Pretend it raised an error!')
    assert str(execinfovalue) == 'TEST APP'
#
# pytest setup stuff
# pytest.main()
#
pytest_sessionstart(session=0, execinfovalue='TEST APP')
#