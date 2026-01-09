from src.models.vehicle import Vehicle


class ElectricCar(Vehicle):
    BASE_PRICE = 5
    COST_PER_MIN = 0.50
    def __init__(self,vehicle_id,model,battery_percentage,seating_capacity,status,distance):
        super().__init__(vehicle_id,model,battery_percentage,status)
        self.seating_capacity = seating_capacity
        self.distance_km = distance

    def calculate_trip_cost(self):
        cost = ElectricCar.BASE_PRICE + ( self.distance_km* (ElectricCar.COST_PER_MIN))
        return  cost
