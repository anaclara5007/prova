# main.py
from funcoes import *

while True:
    print("\n1. Create Vehicle")
    print("2. Read Vehicle")
    print("3. Update Vehicle")
    print("4. Delete Vehicle")
    print("5. Assign Vehicle to Driver")
    print("6. Create Driver")
    print("7. Read Driver")
    print("8. Update Driver")
    print("9. Delete Driver")
    print("10. Get Vehicles for Driver")
    print("11. Print All Vehicles")
    print("12. Print All Drivers")
    print("13. Exit")

    choice = input("\nEnter your choice: ")

    if choice == '1':
        plate = input("Enter plate: ")
        model = input("Enter model: ")
        year = input("Enter year: ")
        create_vehicle(plate, model, year)

    elif choice == '2':
        plate = input("Enter plate: ")
        vehicle = read_vehicle(plate)
        if vehicle:
            print(f"Plate: {vehicle.plate}, Model: {vehicle.model}, Year: {vehicle.year}")

    elif choice == '3':
        plate = input("Enter plate: ")
        model = input("Enter model: ")
        year = input("Enter year: ")
        if update_vehicle(plate, model, year):
            print("Vehicle updated successfully.")
        else:
            print("Vehicle not found.")

    elif choice == '4':
        plate = input("Enter plate: ")
        if delete_vehicle(plate):
            print("Vehicle deleted successfully.")
        else:
            print("Vehicle not found.")

    elif choice == '5':
        vehicle_plate = input("Enter vehicle plate: ")
        driver_license_number = input("Enter driver license number: ")
        if assign_vehicle_to_driver(vehicle_plate, driver_license_number):
            print("Vehicle assigned to driver successfully.")
        else:
            print("Vehicle or driver not found.")

    elif choice == '6':
        name = input("Enter name: ")
        license_number = input("Enter license number: ")
        create_driver(name, license_number)

    elif choice == '7':
        license_number = input("Enter license number: ")
        driver = read_driver(license_number)
        if driver:
            print(f"Name: {driver.name}, License Number: {driver.license_number}")

    elif choice == '8':
        name = input("Enter name: ")
        license_number = input("Enter license number: ")
        if update_driver(name, license_number):
            print("Driver updated successfully.")
        else:
            print("Driver not found.")

    elif choice == '9':
        license_number = input("Enter license number: ")
        if delete_driver(license_number):
            print("Driver deleted successfully.")
        else:
            print("Driver not found.")

    elif choice == '10':
        license_number = input("Enter driver license number: ")
        vehicles = get_driver_vehicles(license_number)
        if vehicles:
            for vehicle in vehicles:
                print(f"Plate: {vehicle.plate}, Model: {vehicle.model}, Year: {vehicle.year}")
        else:
            print("Driver not found or driver has no vehicles assigned.")

    elif choice == '11':
        print_all_vehicles()

    elif choice == '12':
        print_all_drivers()

    elif choice == '13':
        break

    else:
        print("Invalid choice. Please try again.")
