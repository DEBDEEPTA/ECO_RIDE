from src.fleet.hub import FleetHub
from src.fleet.hub_manager import HubManager
from src.models.electric_car import ElectricCar
from src.models.electric_scooter import ElectricScooter

class EcoRideMain:

    @staticmethod
    def greet_user():
        """
            Greets user With Welcome Message
            parameters: None
            returns: None
        """
        print("Welcome to Eco-Ride Urban Mobility System")

    @staticmethod
    def fleet_hub_manager_console_ui():
        """"
            Console ui logic For Managing hub & Vehicle.
            Parameters: None
            Returns: None
        """
        flag = True         # Outer Loop Flag (select Action)

        hub_manager = HubManager()
        while (flag):
            print("Select Action")
            print("\t -> Add Vehicle (press 1)")
            print("\t -> Add hub (press 2)")
            print("\t -> View Hubs (press 3)")
            print("\t -> Exit (press 0)")

            key = input()
            v_flag = True  # Inner Loop Flag (select Vehicle)

            if (key == "0"):
                flag = False

            if key == "1":
                print("Choose Vehicle")
                print("\t -> Add Electric Scooter (press 1)")
                print("\t -> Add Electric Car (press 2)")
                print("\t -> Return (press 0)")
                v_key = input()

                while (v_flag):

                    if v_key == "0":
                        v_flag = False

                    if v_key == "1":
                        vehicle_id = input("Enter Vehicle Id -> ")
                        model = input("Enter Vehicle Model -> ")
                        battery_percentage = int(input("Enter Battery percentage -> "))
                        max_speed_limit = int(input("Enter max speed Limit ->"))
                        scooter_obj = ElectricScooter(vehicle_id, model, battery_percentage, max_speed_limit)

                        hub_name = input("Enter Hub For the vehicle -> ")

                        # Calling get_hub method to obtain hub_name of the hub Object
                        hub = hub_manager.get_hub(hub_name)
                        if hub is None:
                            hub = FleetHub(hub_name)
                            # Calling Method To add Hub Object to hub Manager
                            hub_manager.add_hub(hub)

                        hub.add_vehicle(scooter_obj)
                        break

                    if v_key == "2":
                        vehicle_id = input("Enter Vehicle Id -> ")
                        model = input("Enter Vehicle Model -> ")
                        battery_percentage = int(input("Enter Battery percentage -> "))
                        seating_capacity = int(input("Enter Seating Capacity"))

                        ecar_obj = ElectricCar(vehicle_id, model, battery_percentage, seating_capacity)

                        hub_name = input("Enter Hub For the vehicle -> ")

                        # Calling get_hub method to obtain hub_name of the hub Object
                        hub = hub_manager.get_hub(hub_name)
                        if hub is None:
                            hub = FleetHub(hub_name)
                            # Calling Method To add Hub Object to hub Manager
                            hub_manager.add_hub(hub)

                        hub.add_vehicle(ecar_obj)
                        break

            if (key == "2"):
                    # Adding Hub Logic
                    hub_nm = input("Enter Hub Name -> ")
                    new_hub = FleetHub(hub_nm)
                    hub_manager.add_hub(new_hub)

            if (key == "3"):
                    # View Hub Logic For input Val "3"
                    if (len(hub_manager.hubs) == 0):
                        print("hub Manager is Empty")
                    else:
                        for h_name, h_obj in hub_manager.hubs.items():
                            print(f"{h_name} -> {h_obj.vehicle_list}")






def main():
    # UC1 Greeting user
    EcoRideMain.greet_user()


    # UC5 Showing Dynamic behavior of the abstract method
    # car = ElectricCar(1,"TESLA",83,4)
    # scotter = ElectricScooter(2,"VESVA",54,75)
    #
    # # GETTING VALUE USING GETTER
    # print(car.battery_percentage)
    # # SETING VALUE USING SETTER (VALIDATION CHECK)
    # # car.battery_percentage = -8 # THROWS RUNTIME ERROR 0>=value>=100
    # print(car.battery_percentage)
    #
    # #Dynamic behavior of the abstract method
    # print(car.calculate_trip_cost(35))
    # print(scotter.calculate_trip_cost(35))

    # UC6 -> Use Console to add a new Hub or add vehicles to an existing Hub.

    EcoRideMain.fleet_hub_manager_console_ui()


if __name__=="__main__":
    main()