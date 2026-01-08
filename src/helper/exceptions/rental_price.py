class InvalidRentalPriceError(Exception):
    def __init__(self, message = "Invalid Rental Price"):
        self.message = message
        super().__init__(message)