from abc import ABC, abstractmethod
class Vehicle:
    def __init__(self, vehicle_id, model,b_percentage):
        self.vehicle_id = vehicle_id
        self.model = model
        self.battery_percentage = b_percentage

        self.__maintenance_status = None
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
            raise RuntimeError("Battery percentage cannot be more than 100 or less than 0")

    @property
    def rental_price(self):
        return self.__rental_price

    @rental_price.setter
    def rental_price(self,price):
        if(price > 0):
            self.__rental_price = price
        else:
            raise RuntimeError("Rental Price Must be More Than 0")


    @abstractmethod
    def calculate_trip_cost(self,distance):
        pass


    def __str__(self):
        return (f"{self.__class__.__name__} ->"
                f"id: {self.vehicle_id},"
                f"name: {self.model},"
                f"battery: {self.__battery_percentage}")

    def __repr__(self):
        return self.__str__()
