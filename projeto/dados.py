# dados.py

class Vehicle:
    def __init__(self, plate, model, year):
        self.plate = plate
        self.model = model
        self.year = year
        self.driver = None

class Driver:
    def __init__(self, name, license_number):
        self.name = name
        self.license_number = license_number
        self.vehicles = []
