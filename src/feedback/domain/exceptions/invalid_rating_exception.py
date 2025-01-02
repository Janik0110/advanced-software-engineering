class InvalidRatingException(Exception):
    def __init__(self, message: str = "Invalid rating"):
        super().__init__(message)
