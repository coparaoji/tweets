
import sys
import pytest
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath('../factory.py'))
sys.path.append(os.path.dirname(SCRIPT_DIR))
sys.path.append('../tweets')
from ..db import dbs
from tweets.app import app
from tweets.src import tweets

class TestConnections:
    ''' A class to test connections to database and apis. '''

    def testDatabaseConn(self):
        try:
            result="success"
            print(os.environ.get('DATABASE_PATH'))
            dbs.create_connection()
        except Exception as e:
            result = e
        finally:
            assert result=="success"

    def testTweepyConn(self):
        try:
            result="success"
            c = tweets.Tweets()
            c.search_player('Lebron James',(0,1,0))
        except Exception as e:
            result = e
        finally:
            assert result=="success"


class TestDataContent:
    data = dbs.get_data()

    def test_data_size(self):
        size = len(self.data)
        assert size>0

    def test_data_var_type(self):
        assert isinstance(self.data,list)

    def test_data_type0(self):
        assert isinstance(self.data[0][0],str)

    def test_data_type1(self):
        assert isinstance(self.data[0][1],str)

    def test_data_type2(self):
        assert isinstance(self.data[0][2],int)
        
    def test_data_type3(self):
        assert isinstance(self.data[0][3],float)




@pytest.fixture()
def client():
    # Used with tests to create an application to tests requests on.
    with app.test_client() as client:
        yield client

class TestDevServerDeployment:
    def test_request_example(self,client): 
        response = client.get("/")

        assert 200 == response.status_code

