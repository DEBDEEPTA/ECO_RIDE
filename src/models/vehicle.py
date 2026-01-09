from abc import ABC, abstractmethod

from src.helper.enums.vehicle_status import VehicleStatus
from src.helper.exceptions.battery_level import BatteryLevelError
from src.helper.exceptions.rental_price import InvalidRentalPriceError


class Vehicle:
    def __init__(self, vehicle_id, model,b_percentage,status:VehicleStatus):
        self.vehicle_id = vehicle_id
        self.model = model
        # assigning value to the setter of battery_percentage
        self.battery_percentage = b_percentage

        # assassinating value to the setter (property) of the __maintenance Status
        self.maintenance_status = status

        self.__rental_price = None

    @property
    def maintenance_status(self):
            return self.__maintenance_status


    @maintenance_status.setter
    def maintenance_status(self,maintenance_status):
            self.__maintenance_status = maintenance_status

    @property
    def battery_percentage(self):
        return self.__battery_percentage

    @battery_percentage.setter
    def battery_percentage(self,value):
        if (100 >= value >= 0):
            self.__battery_percentage = value
        else:
            raise BatteryLevelError()

    @property
    def rental_price(self):
        return self.__rental_price

    @rental_price.setter
    def rental_price(self,price):
           if (price > 0):
               self.__rental_price = price
           else:
               raise InvalidRentalPriceError


    @abstractmethod
    def calculate_trip_cost(self):
        pass

    def __str__(self):
        return (f"\n{self.__class__.__name__}:("
                f"id: {self.vehicle_id} "
                f"name: {self.model} "
                f"battery: {self.__battery_percentage})\n")

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if not isinstance(other,Vehicle):
            return False
        else:
            return self.vehicle_id == other.vehicle_id
