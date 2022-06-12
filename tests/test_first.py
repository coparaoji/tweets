
import sys
import pytest
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath('../factory.py'))
sys.path.append(os.path.dirname(SCRIPT_DIR))
sys.path.append('.../tweets')
from ..db import dbs


class TestDataRetrieval:
    data = dbs.get_data()

    def test_data_var_type(self):
        assert isinstance(self.data,list)

    def test_data_size(self):
        size = len(self.data)
        assert size>0

class TestDataContent:
    data = dbs.get_data()
    data = data[0]

    def test_data_type0(self):
        assert isinstance(self.data[0],str)

    def test_data_type1(self):
        assert isinstance(self.data[1],str)

    def test_data_type2(self):
        assert isinstance(self.data[2],int)
        
    def test_data_type3(self):
        assert isinstance(self.data[3],float)



from tweets.app import app

@pytest.fixture()
def client():
    with app.test_client() as client:
        yield client

class TestCode:
    def test_request_example(self,client):
        
        response = client.get("/")

        assert 200 == response.status_code

