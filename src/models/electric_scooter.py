from src.models.vehicle import Vehicle


class ElectricScooter(Vehicle):
    def __init__(self,vehicle_id,model,battery_percentage,max_speed_limit,status):
        super().__init__(vehicle_id, model, battery_percentage,status)
        self.max_speed_limit = max_speed_limit

    def calculate_trip_cost(self,distance_in_min):
        base = 1
        cost = base + (distance_in_min*0.15)
        return cost