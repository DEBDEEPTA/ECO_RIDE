import pytest
import  src.fleet.hub_manager as hb
from tests.conftest import get_test_hub

class TestUnits:
    test_hub_manager = hb.HubManager()

    def setup_method(self,method):
        print(f"test started : {method.__name__}")

    def teardown_method(self,method):
        print(f"test closed : {method.__name__}")

    @pytest.mark.parametrize("name", ["RACHI", "DELHI", "AGRA"])
    def test_add_hub_to_manager(self, name, get_test_hub, hub_manager):
        test_hub = get_test_hub(name)
        hub_manager.add_hub(test_hub)
        hub = hub_manager.hubs.get(name)
        assert hub.hub_name == name

    @pytest.mark.parametrize("name", ["RACHI", "DELHI", "AGRA"])
    def test_get_hub_name(self, name, hub_manager, get_test_hub):
        hub = get_test_hub(name)
        hub_manager.add_hub(hub)
        fetched_hub = hub_manager.get_hub(name)
        assert fetched_hub.hub_name == name
