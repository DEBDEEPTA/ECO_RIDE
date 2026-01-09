from src.models.vehicle import Vehicle


class ElectricCar(Vehicle):

    def __init__(self,vehicle_id,model,battery_percentage,seating_capacity,status):
        super().__init__(vehicle_id,model,battery_percentage,status)
        self.seating_capacity = seating_capacity

    def calculate_trip_cost(self,distance_in_km):
        base = 5
        cost = base + (distance_in_km * 0.50)
        return  cost
