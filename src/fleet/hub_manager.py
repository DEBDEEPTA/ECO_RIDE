class HubManager:
    def __init__(self):
        self.hubs = {}

    def add_hub(self,hub):
        self.hubs[hub.hub_name] = hub.vehicle_list