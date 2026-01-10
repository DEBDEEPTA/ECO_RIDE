from src.helper.io_utils.csv_writer import save_data
from src.fleet.hub import FleetHub
from src.fleet.hub_manager import HubManager
from src.helper.enums.vehicle_status import VehicleStatus
from src.helper.exceptions.battery_level import BatteryLevelError
from src.helper.exceptions.vehicle_exists import VehicleExistsError
from src.helper.io_utils.csv_writer import load_data
from src.models.electric_car import ElectricCar
from src.models.electric_scooter import ElectricScooter

class EcoRideMain:

    @staticmethod
    def greet_user():
        """
        Display a welcome message for the Eco-Ride Urban Mobility System.
        """

        print("Welcome to Eco-Ride Urban Mobility System")
        print("=" * 40)

    @staticmethod
    def console_ui_comp_search_filter(hub_manager):
        """
          Display console-based menu options for searching vehicles.
          Args:
              hub_manager: HubManager instance consists of all the hubs in which user want to search by the specific filter.
          Returns:
              None
          """
        print("Select Search Filter")
        print("=" * 40)
        print("\t 1. Search Vehicles By Hub")
        print("\t 2. Search Vehicle By Battery Percentage")
        print("\t 0. Return")

        choice = input()
        vehicles = None
        if(choice == "0"):
            return
        if(choice == "1"):
            print("Search Vehicles By Hub")
            print("=" * 40)
            hub_name = input("\tEnter hub Name ->")
            vehicles = hub_manager.search_vehicle_by_hub_name(hub_name)

        elif (choice == "2"):
            print("Search Vehicles By Battery Percentage")
            print("=" * 40)
            battery_level = int(input("\tEnter Minimum Battery Percentage ->"))
            vehicles = hub_manager.search_by_min_battery_level(battery_level)

        if vehicles:
            for v in vehicles:
                print(v)
        else:
            print("No Vehicles found")

    @staticmethod
    def console_ui_comp_vehicle_categorization(hub_manager):
        categorized = hub_manager.vehicle_type_catagory()

        if not categorized:
            print("No vehicles available")
        else:
            for v_type, vehicles in categorized.items():
                print(f"\n{v_type} Vehicles")
                print("=" * 40)
                for v in vehicles:
                    print(v)

    @staticmethod
    def console_ui_comp_vehicle_status_group(hub_manager):
        status_count_analysis = hub_manager.vehicle_count_by_status()
        print("\nFleet Analytics Summary")
        print("=" * 40)

        print(f"Available Vehicles        : {status_count_analysis.get(VehicleStatus.AVAILABLE, 0)}")
        print(f"Vehicles On Trip          : {status_count_analysis.get(VehicleStatus.ON_TRIP, 0)}")
        print(f"Under Maintenance Vehicles: {status_count_analysis.get(VehicleStatus.UNDER_MAINTENANCE, 0)}")

    @staticmethod
    def console_ui_comp_maintance_status_ip():
        m_status = VehicleStatus.AVAILABLE
        print("Select Vehicle Status")
        print("-" * 40)
        print("\t 1. Available")
        print("\t 2. On Trip")
        print("\t 3. under Maintenance")
        status = input()
        if (status == "1"):
            m_status = VehicleStatus.AVAILABLE
        elif (status == "2"):
            m_status = VehicleStatus.ON_TRIP
        elif (status == "3"):
            m_status = VehicleStatus.UNDER_MAINTENANCE

        return m_status

    @staticmethod
    def console_ui_comp_vehicle_sort(hub_manager):
        hub_name = input("Enter Hub Name -> ")
        hub = hub_manager.get_hub(hub_name)
        if hub:
            sorted_list = []
            print("Sorting Options")
            print("=" * 40)
            print("\t 1. Sort by Model Name (Descending)")
            print("\t 2. Sort by Battery (Descending)")
            print("\t 3. Sort by Fare (Descending)")
            print("\t 0. Return")
            choice = input()
            choice_name = None
            if(choice == "0"):
                return
            elif(choice == "1"):
                sorted_list = hub.get_sorted_vehicles_by_model()
                choice_name = "Model"
            elif(choice == "2"):
                sorted_list = hub.get_vehicles_by_battery()
                choice_name = "Battery"
            elif (choice == "3"):
                sorted_list = hub.get_vehicles_sorted_by_fare()
                choice_name = "Fare"

            print(f"\nVehicles in Hub '{hub_name}' (Sorted by {choice_name}):")
            print("-" * 40)
            for v in sorted_list:
                print(v)
        else:
            print("Hub not found")

    @staticmethod
    def fleet_hub_manager_console_ui(hub_manager):
        """"
            Console ui logic For Managing hub & Vehicle.
            Param:
                None
            Returns:
                None
        """
        flag = True         # Outer Loop Flag (select Action)
        while (flag):

            print("Select Action")
            print("=" * 40)
            print("\t 1. Add Vehicle")
            print("\t 2. Add hub")
            print("\t 3. View Hubs")
            print("\t 4. Search Vehicles")
            print("\t 5. Categorize Vehicles By Type")
            print("\t 6. Categorize Vehicles By Status")
            print("\t 7. Order Vehicles")
            print("\t 0. Exit")

            key = input()
            v_flag = True  # Inner Loop Flag (select Vehicle)

            if (key == "0"):
                flag = False

            if key == "1":
                print("Choose Vehicle")
                print("=" * 40)
                print("\t 1. Add Electric Scooter ")
                print("\t 2. Add Electric Car ")
                print("\t 0. Return ")
                v_key = input()

                while (v_flag):

                    if v_key == "0":
                        v_flag = False

                    if v_key == "1":
                        scooter_obj = None
                        while(True):
                            #Handeling BatteryLevel Error
                            try:
                                vehicle_id = input("Enter Vehicle Id -> ")
                                model = input("Enter Vehicle Model -> ")
                                battery_percentage = int(input("Enter Battery percentage -> "))
                                max_speed_limit = int(input("Enter max speed Limit -> "))
                                m_status = EcoRideMain.console_ui_comp_maintance_status_ip()
                                distance = int(input("Enter distance travelled -> "))
                                scooter_obj = ElectricScooter(vehicle_id, model, battery_percentage, max_speed_limit,m_status,distance)
                            except BatteryLevelError:
                                print("Battery percentage Should be in range 0 to 100")
                            else:
                                break

                        hub_name = input("Enter Hub For the vehicle -> ")

                        # Calling get_hub method to obtain hub_name of the hub Object
                        hub = hub_manager.get_hub(hub_name)
                        if hub is None:
                            hub = FleetHub(hub_name)
                            # Calling Method To add Hub Object to hub Manager
                            hub_manager.add_hub(hub)
                        # Handling VehicleExistError (If vehicle with same id exist with in a hub)
                        try:
                            hub.add_vehicle(scooter_obj)
                        except VehicleExistsError as e:
                            print(e)
                        else:
                            break

                    if v_key == "2":
                        ecar_obj = None
                        while (True):
                            # Handeling BatteryLevel Error
                            try:
                                vehicle_id = input("Enter Vehicle Id -> ")
                                model = input("Enter Vehicle Model -> ")
                                battery_percentage = int(input("Enter Battery percentage -> "))
                                seating_capacity = int(input("Enter Seating Capacity -> "))
                                m_status = EcoRideMain.console_ui_comp_maintance_status_ip()
                                distance = int(input("Enter distance travelled -> "))
                                ecar_obj = ElectricCar(vehicle_id, model, battery_percentage, seating_capacity,m_status,distance)
                            except BatteryLevelError:
                                print("Battery percentage Should be in range 0 to 100")
                            else:
                                break

                        hub_name = input("Enter Hub For the vehicle -> ")

                        # Calling get_hub method to obtain hub_name of the hub Object
                        hub = hub_manager.get_hub(hub_name)
                        if hub is None:
                            hub = FleetHub(hub_name)
                            # Calling Method To add Hub Object to hub Manager
                            hub_manager.add_hub(hub)

                        try:
                            hub.add_vehicle(ecar_obj)
                        except VehicleExistsError as e:
                            print(e)
                        else:
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

            if(key == "4"):
                EcoRideMain.console_ui_comp_search_filter(hub_manager)
            if(key == "5"):
                EcoRideMain.console_ui_comp_vehicle_categorization(hub_manager)
            if(key == "6"):
                EcoRideMain.console_ui_comp_vehicle_status_group(hub_manager)
            if(key == "7"):
                EcoRideMain.console_ui_comp_vehicle_sort(hub_manager)

if __name__ == "__main__":

    #UC1 Greeting user
    EcoRideMain.greet_user()
    # Creating Hub Manager
    hub_mnager = HubManager()
    # loading csv data
    try:
        load_data(hub_mnager, "vehicle_data.csv")
        print("Fleet data loaded successfully")
    except FileNotFoundError:
        print("No existing fleet data found")

    # UC6 -> Use Console to add a new Hub or add vehicles to an existing Hub.
    EcoRideMain.fleet_hub_manager_console_ui(hub_mnager)

    # saving csv data
    save_data(hub_mnager, "vehicle_data.csv")
    print("Fleet data saved successfully")
