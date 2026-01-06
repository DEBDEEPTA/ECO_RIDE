from sys import flags

from src.fleet.hub import FleetHub
from src.fleet.hub_manager import HubManager
from src.models.electric_car import ElectricCar
from src.models.electric_scooter import ElectricScooter


class EcoRideMain:
    def greet(self):
        print("Welcome to Eco-Ride Urban Mobility System")




def main():
    ec_ride = EcoRideMain()
    # UC1 Greeting user
    ec_ride.greet()
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
    flag = True

    hub_manager = HubManager()

    while(flag):
        print("Select Action")
        print("\t -> Add Vehicle (press 1)")
        print("\t -> Add hub (press 2)")
        print("\t -> View Hubs (press 3)")
        print("\t -> Exit (press 0)")

        key = input()

        if(key == "0"):
            flag = False

        if key == "1":
            print("Choose Vehicle")
            print("\t -> Add Electric Scooter (press 1)")
            print("\t -> Add Electric Car (press 2)")
            print("\t -> Exit (press 0)")
            v_key = input()


            if v_key == "0":
                flag = False
            if v_key == "1":
                vehicle_id = input("Enter Vehicle Id -> ")
                model = input("Enter Vehicle Model -> ")
                battery_percentage = int(input("Enter Battery percentage -> "))
                max_speed_limit = int(input("Enter max speed Limit ->"))
                scooter_obj = ElectricScooter(vehicle_id,model,battery_percentage,max_speed_limit)

                hub_name = input("Enter Hub For the vehicle -> ")

                hub = FleetHub(hub_name)
                hub.add_vehicle(scooter_obj)
                hub_manager.add_hub(hub)

            if v_key == "2":
                vehicle_id = input("Enter Vehicle Id -> ")
                model = input("Enter Vehicle Model -> ")
                battery_percentage = int(input("Enter Battery percentage -> "))
                seating_capacity = int(input("Enter Seating Capacity"))

                ecar_obj = ElectricCar(vehicle_id,model,battery_percentage,seating_capacity)

                hub_name = input("Enter Hub For the vehicle -> ")
                hub = FleetHub(hub_name)
                hub.add_vehicle(ecar_obj)
                hub_manager.add_hub(hub)

        if( key == "2"):
            hub_nm = input("Enter Hub Name -> ")
            new_hub = FleetHub(hub_nm)
            hub_manager.add_hub(new_hub)
        if (key == "3"):

            if (len(hub_manager.hubs) == 0):
                print("hub Manager is Empty")
            else:
                for k, v in hub_manager.hubs.items():
                    print(f"{k} -> {v}")










if __name__=="__main__":
    main()