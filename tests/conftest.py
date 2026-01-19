import pytest

import src.fleet.hub as hb
import  src.fleet.hub_manager as hbm
@pytest.fixture
def get_test_hub():
    def build(name):
        test_hub = hb.FleetHub(name)
        return test_hub
    return  build

@pytest.fixture
def hub_manager():
    return hbm.HubManager()
