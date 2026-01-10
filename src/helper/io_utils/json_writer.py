import json
from xml.etree.ElementTree import indent

from src.fleet.hub import FleetHub
from src.helper.enums.vehicle_status import VehicleStatus
from src.models.electric_car import ElectricCar
from src.models.electric_scooter import ElectricScooter


def write_json_file(hub_manager,file_path):

    with open(file_path, "w") as writer_obj:
        json.dump(hub_manager.to_dict(), writer_obj, indent=4)




def load_json_file(hub_manager,file_path):
    with open( file_path, "r") as reader_obj:
        data = json.load(reader_obj)

        for hub_name, hub_data in data.items():
            hub = FleetHub(hub_name)

            for v in hub_data["vehicle_list"]:
                status = VehicleStatus[v["maintenance_status"]]

                if v["vehicle_type"] == "ElectricCar":
                    vehicle = ElectricCar(
                        v["vehicle_id"],
                        v["model"],
                        v["battery_percentage"],
                        v["seating_capacity"],
                        status,
                        v["distance"]
                    )

                elif v["vehicle_type"] == "ElectricScooter":
                    vehicle = ElectricScooter(
                        v["vehicle_id"],
                        v["model"],
                        v["battery_percentage"],
                        v["max_speed_limit"],
                        status,
                        v["distance"]
                    )

                hub.add_vehicle(vehicle)

            hub_manager.add_hub(hub)