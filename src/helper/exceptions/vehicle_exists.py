class VehicleExistsError(Exception):
        def __init__(self,message = "Duplicate vehicle"):
            self.message = message
            super().__init__(message)