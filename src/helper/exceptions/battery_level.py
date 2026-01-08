class BatteryLevelError(Exception):
    def __init__(self,message="Invalid Battery Percentage"):
        self.message = message
        super().__init__(message)