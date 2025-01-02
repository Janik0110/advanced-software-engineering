class InvalidPostalCodeException(Exception):
    def __init__(self, postal_code: str):
        super().__init__(f"Invalid postal code: {postal_code}")
