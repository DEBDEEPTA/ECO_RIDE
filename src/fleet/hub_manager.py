class HubManager:
    def __init__(self):
        self.hubs = {}

    def add_hub(self,hub):
        self.hubs[hub.hub_name] = hub

    def get_hub(self,hub_name):
        return self.hubs.get(hub_name)