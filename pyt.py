import pytest

@pytest.fixture()
def my_fixture1():
    print "\nI'm the 1stfixture"


@pytest.fixture()
def my_fixture2():
    print "\nI'm the 2ndfixture"
	
@pytest.mark.usefixtures('my_fixture1')
class Test:
    def test1(self):
        print "I'm the test 1"

    def test2(self):
        print "I'm the test 2"
#Amrendra Singh