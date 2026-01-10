import csv
from src.fleet.hub import FleetHub
from src.helper.enums.vehicle_status import VehicleStatus
from src.models.electric_car import ElectricCar
from src.models.electric_scooter import ElectricScooter

def save_data(hub_manager,path):
    """
    Save all hubs and vehicles into CSV file.
    """

    with open(path, mode="w", newline="") as file:
        writer = csv.writer(file)


        writer.writerow([
            "hub_name", "vehicle_type", "vehicle_id", "model",
            "battery", "status", "distance", "seating_cap_or_max_speed"
        ])

        for h_name, hub in hub_manager.hubs.items():
            for v in hub.vehicle_list:
                if isinstance(v, ElectricCar):
                    vehicle_type = "ElectricCar"
                    distance_trvl = v.distance_km
                    child_attr = v.seating_capacity

                elif isinstance(v, ElectricScooter):
                    vehicle_type = "ElectricScooter"
                    distance_trvl = v.distance_min
                    child_attr = v.max_speed_limit

                writer.writerow([
                    h_name,
                    vehicle_type,
                    v.vehicle_id,
                    v.model,
                    v.battery_percentage,
                    v.maintenance_status.name,
                    distance_trvl,
                    child_attr

                ])

def load_data(hub_manager,path):
    """
        loads csv file for the vehicles
    """
    with open(path, mode="r") as file:

        reader_data = csv.DictReader(file)

        for row in reader_data:
            hub_name = row["hub_name"]

            hub = hub_manager.get_hub(hub_name)
            if hub is None:
                hub = FleetHub(hub_name)
                hub_manager.add_hub(hub)

            status_val = VehicleStatus[row["status"]] # CONVERTED STRING TO ENUM

            if row["vehicle_type"] == "ElectricCar":
                # SETTING ElectricCar Constructor
                vehicle = ElectricCar(
                    vehicle_id=row["vehicle_id"],
                    model=row["model"],
                    battery_percentage=int(row["battery"]),
                    status=status_val,
                    seating_capacity=int(row["seating_cap_or_max_speed"]),
                    distance=float(row["distance"])
                )

            else:
                vehicle = ElectricScooter(
                    # SETTING ElectricScooter Constructor
                    vehicle_id=row["vehicle_id"],
                    model=row["model"],
                    battery_percentage=int(row["battery"]),
                    status=status_val,
                    max_speed_limit=int(row["seating_cap_or_max_speed"]),
                    distance=float(row["distance"])
                )

            hub.add_vehicle(vehicle)