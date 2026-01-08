from src.helper.exceptions.vehicle_exists import VehicleExistsError


class FleetHub:
    def __init__(self,hub_name):
        # HUB NAME
        self.hub_name = hub_name
        # VEHICLE LIST FOR EACH HUB
        self.vehicle_list = []


    def add_vehicle(self,vehicle):
        if vehicle in self.vehicle_list:
            raise VehicleExistsError(f"vehicle id:{vehicle.vehicle_id} is already present in hub:{self.hub_name}")

        self.vehicle_list.append(vehicle)
