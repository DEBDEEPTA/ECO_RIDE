from src.models.vehicle import Vehicle


class ElectricScooter(Vehicle):
    BASE_PRICE = 1
    COST_PER_MIN = 0.15
    def __init__(self,vehicle_id,model,battery_percentage,max_speed_limit,status,distance):
        super().__init__(vehicle_id, model, battery_percentage,status)
        self.max_speed_limit = max_speed_limit
        self.distance_min = distance


    def calculate_trip_cost(self):
        cost = ElectricScooter.BASE_PRICE + (self.distance_min * (ElectricScooter.COST_PER_MIN))
        return cost