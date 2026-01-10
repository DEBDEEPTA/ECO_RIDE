from collections import defaultdict
from src.models.electric_car import ElectricCar
from src.models.electric_scooter import ElectricScooter

class HubManager:
    def __init__(self):
        self.hubs = {}

    def add_hub(self,hub):
        self.hubs[hub.hub_name] = hub

    def get_hub(self,hub_name):
        return self.hubs.get(hub_name)

    def search_vehicle_by_hub_name(self,hub_name):
        """
        Search and return all vehicles available in the specified fleet hub.

        Args:
            hub_name: Name of the fleet hub to search vehicles in.

        Returns:
            list[Vehicle]: A list of vehicles present in the given hub.
                           Returns an empty list if the hub name is not found
        """
        hub = self.hubs.get(hub_name)  # returns value of the key
                                       # Default returns None
        if not hub:
            return []                  # return empty List if no hub with key value Found
        return hub.vehicle_list        # return's vehicle List of the hub

    def search_by_min_battery_level(self,min_battery=80):
        """
        Search and return vehicles whose battery level is greater than or equal
        to the specified minimum battery percentage.

        Args:
            min_battery: Minimum battery percentage required Defaults to 80.

        Returns:
            list[Vehicle]: A list of vehicles with min battery level
                           Returns an empty list if no vehicles match.
        """
        result = []
        for hub in self.hubs.values():    # obtain value for each hub name

            filtered_result = filter( lambda b: b.battery_percentage >= min_battery,
                                      hub.vehicle_list)
            result.extend(filtered_result) # add filtered elements to the result list
        return  result

    def vehicle_type_catagory(self):
        """
            Categorize and group vehicles by their type (Car / Scooter).
            Returns:
                dict[]: Dictionary of vehicle type to list of vehicles.
        """

        category_dict = defaultdict(list)   # Default Dict is used to avoid KeyError

        for hub in self.hubs.values():
            for v in hub.vehicle_list:

                if isinstance(v,ElectricCar):
                    category_dict["Electric Car"].append(v)

                elif isinstance(v,ElectricScooter):
                    category_dict["Electric Scooter"].append(v)

        return dict(category_dict)

    def vehicle_count_by_status(self):
        """
               Count vehicles by their current status using Enum types.
        """
        status_count = defaultdict(int)

        for hub in self.hubs.values():
            for v in hub.vehicle_list:
                status_count[v.maintenance_status] += 1  # Calling getter (property) of the __maintenance_status

        return dict(status_count)

    def to_dict(self):
        #Dictionary Comprehension
        data =  { hub_name:hub.to_dict() for hub_name, hub in self.hubs.items()}
        return data