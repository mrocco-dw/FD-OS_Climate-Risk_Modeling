#
# conftest.py
#
import pytest
#
def pytest_sessionstart(session=0):
    with pytest.raises(ValueError) as execinfo: 
        execinfo.value = 'TEST APP'
    assert str(execinfo.value) == 'TEST APP'
#    pass
#    return 1
#
# pytest setup stuff
#pytest.main()
#