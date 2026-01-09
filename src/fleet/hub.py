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

    def get_sorted_vehicles_by_model(self):
        """
        Return a new list of vehicles sorted alphabetically by model name.
        """

        return sorted(self.vehicle_list, key=lambda v: v.model.lower())
