import pytest

from src.fleet.hub import FleetHub
from src.helper.enums.vehicle_status import VehicleStatus
from src.helper.exceptions.battery_level import BatteryLevelError
from src.helper.exceptions.rental_price import InvalidRentalPriceError
from src.helper.exceptions.vehicle_exists import VehicleExistsError
from src.models.vehicle import Vehicle


class TestExceptions:

    def setup_method(self,method):
        print(f"test started : {method.__name__}")

    def teardown_method(self,method):
        print(f"test closed : {method.__name__}")


    @pytest.mark.parametrize("vehicle_id, model, b_percentage, status",[("KA0534B","Tata",-8,VehicleStatus.AVAILABLE),
                                                                        ("KA0584C","MG",-1,VehicleStatus.AVAILABLE),
                                                                        ("WB33C01","Mahindra",199,VehicleStatus.AVAILABLE)
                                                                        ])
    def test_battery_level_exception(self,vehicle_id, model, b_percentage, status):

       with pytest.raises(BatteryLevelError):
           v = Vehicle(vehicle_id, model, b_percentage, status)


    @pytest.mark.parametrize("price",[-1,-3234, 0])
    def test_rental_price_exception(self,price):
        v = Vehicle("KA0534B","Tata",89,VehicleStatus.UNDER_MAINTENANCE)
        with pytest.raises(InvalidRentalPriceError):
            v.rental_price = price

    @pytest.mark.parametrize("vehicle_id, model, b_percentage, status",
                             [("KA0534C", "Tata", 78, VehicleStatus.AVAILABLE),
                              ("KA0534B", "MG", 100, VehicleStatus.AVAILABLE),
                              ("WB33C01", "Mahindra", 89, VehicleStatus.AVAILABLE)
                              ])
    def test_vehicle_exist_exception(self,vehicle_id, model, b_percentage, status):
        v = Vehicle(vehicle_id, model, b_percentage, status)
        hub = FleetHub("TEST_HUB")
        hub.add_vehicle(v)
        with pytest.raises(VehicleExistsError):
            hub.add_vehicle(v)