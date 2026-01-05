from sys import flags

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
    car = ElectricCar(1,"TESLA",83,4)
    scotter = ElectricScooter(2,"VESVA",54,75)

    # GETTING VALUE USING GETTER
    print(car.battery_percentage)
    # SETING VALUE USING SETTER (VALIDATION CHECK)
    # car.battery_percentage = -8 # THROWS RUNTIME ERROR 0>=value>=100
    print(car.battery_percentage)

    #Dynamic behavior of the abstract method
    print(car.calculate_trip_cost(35))
    print(scotter.calculate_trip_cost(35))






if __name__=="__main__":
    main()