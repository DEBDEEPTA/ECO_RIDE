class FleetHub:
    def __init__(self,hub_name):
        # HUB NAME
        self.hub_name = hub_name
        # VEHICLE LIST FOR EACH HUB
        self.vehicle_list = []


    def add_vehicle(self,vehicle):
        self.vehicle_list.append(vehicle)

