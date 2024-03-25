# funcoes.py
from dados import Vehicle, Driver

vehicles = []
drivers = []

def create_vehicle(plate, model, year):
    vehicle = Vehicle(plate, model, year)
    vehicles.append(vehicle)
    return vehicle

def read_vehicle(plate):
    for vehicle in vehicles:
        if vehicle.plate == plate:
            return vehicle
    return None

def update_vehicle(plate, model, year):
    vehicle = read_vehicle(plate)
    if vehicle:
        vehicle.model = model
        vehicle.year = year
        return True
    return False

def delete_vehicle(plate):
    vehicle = read_vehicle(plate)
    if vehicle:
        vehicles.remove(vehicle)
        return True
    return False

def assign_vehicle_to_driver(vehicle_plate, driver_license_number):
    vehicle = read_vehicle(vehicle_plate)
    driver = read_driver(driver_license_number)
    if vehicle and driver:
        if vehicle.driver:
            vehicle.driver.vehicles.remove(vehicle)
        vehicle.driver = driver
        driver.vehicles.append(vehicle)
        return True
    return False

def create_driver(name, license_number):
    driver = Driver(name, license_number)
    drivers.append(driver)
    return driver

def read_driver(license_number):
    for driver in drivers:
        if driver.license_number == license_number:
            return driver
    return None

def update_driver(name, license_number):
    driver = read_driver(license_number)
    if driver:
        driver.name = name
        return True
    return False

def delete_driver(license_number):
    driver = read_driver(license_number)
    if driver:
        drivers.remove(driver)
        return True
    return False

def get_vehicles_for_driver(driver_license_number):
    driver = read_driver(driver_license_number)
    if driver:
        return driver.vehicles
    return None

def print_all_vehicles():
    for vehicle in vehicles:
        print(f"Plate: {vehicle.plate}, Model: {vehicle.model}, Year: {vehicle.year}")

def print_all_drivers():
    for driver in drivers:
        print(f"Name: {driver.name}, License Number: {driver.license_number}")

