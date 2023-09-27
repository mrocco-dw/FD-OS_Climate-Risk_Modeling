#
# conftest.py
#
import pytest
#
def pytest_sessionstart(session=0):
    execinfovalue = ""
    with pytest.raises(ValueError) as execinfo: 
        execinfovalue = 'TEST APP'
    assert str(execinfovalue) == 'TEST APP'
#    pass
#    return 1
#
# pytest setup stuff
#pytest.main()
#