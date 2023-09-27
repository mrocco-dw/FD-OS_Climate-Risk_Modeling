#
# conftest.py
#
import pytest
#
def pytest_sessionstart(session=0, execinfovalue='TEST APP'):
    #with pytest.raises(ValueError) as execinfo: 
    #    execinfo.value = 'TEST APP'
    assert str(execinfovalue) == 'TEST APP'
#    pass
#    return 1
#
# pytest setup stuff
pytest.main()
#
pytest_sessionstart(session=0, execinfovalue='TEST APP')
#