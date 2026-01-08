class HubManager:
    def __init__(self):
        self.hubs = {}

    def add_hub(self,hub):
        self.hubs[hub.hub_name] = hub

    def get_hub(self,hub_name):
        return self.hubs.get(hub_name)

    def search_vehicle_by_hub_name(self,hub_name):
        """
        Search and return all vehicles available in a specific fleet hub.
        param
            hub_name: string input of the hub Name
        returns
            list[Vehicle]: list of vehicles present in the hub
            list[]: empty list if hub is not found
        """
        hub = self.hubs.get(hub_name)  # returns value of the key
                                       # Default returns None
        if not hub:
            return []                  # return empty List if no hub with key value Found
        return hub.vehicle_list        # return's vehicle List of the hub

    def search_by_min_battery_level(self,min_battery=80):
        """
        Display Vehicles which only have minimus specified battery
        param
            min_battery: min battery level for the vehicle, default value is 80
        returns
            list[Vehicle]: list of vehicles having min_battery or more
            list[]: empty list if no vehicles found with the specified battery percentage
        """
        result = []
        for hub in self.hubs.values():    # obtain value for each hub name

            filtered_result = filter( lambda b: b.battery_percentage > min_battery,
                                      hub.vehicle_list)
            result.extend(filtered_result) # add filtered elements to the result list
        return  result