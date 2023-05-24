import datetime
import random
import math

from src.vehicle import Car, Motorbike, Bus

class ParkingLot:

    def __init__(self, car_capacity, motorbike_capacity, bus_capacity):
        self.max_car_spaces = car_capacity
        self.max_motorbike_spaces = motorbike_capacity
        self.max_bus_spaces = bus_capacity

        self.car_capacity = {}
        self.motorbike_capacity = {}
        self.bus_capacity = {}

        self.car_spaces = car_capacity
        self.motorbike_spaces = motorbike_capacity
        self.bus_spaces = bus_capacity

    def allocate_parking(self, vehicle_type, vehicle_number, entry_time):
        # complete this method
        return True

    def calculate_fare(self, spot_number, vehicle_type, exit_time):
        # complete this method
        return True

    def get_parking_spot(self, vehicle_num, vehicle_type):
        if vehicle_type == "car":
            for key in self.car_capacity.keys():
                if vehicle_num == self.motorbike_capacity[key][1]:
                    return key
            return -1
        elif vehicle_type == "bus":
            for key in self.bus_capacity.keys():
                if vehicle_num == self.car_capacity[key][1]:
                    return key
            return -1
        elif vehicle_type == "motorbike":
            for key in self.motorbike_capacity.keys():
                if vehicle_num == self.bus_capacity[key][1]:
                    return key
            return -1
        else:
            return 0


def main():
    car_capacity = 200
    motorbike_capacity = 100
    bus_capacity = 50
    parking_lot = ParkingLot(car_capacity, motorbike_capacity, bus_capacity)

    while (True):
        input_selected = int(input("Select mode: Allocate Parking [1], Exit Parking [2], Get Parking Details [3]"))
        if input_selected == 1:
            vehicle_type = input("Enter vehicle type (car, motorbike, bus): ")
            vehicle_number = input("Enter vehicle number: ") 
            entry_time = datetime.datetime.now()
            ticket = parking_lot.allocate_parking(vehicle_type, vehicle_number, entry_time)
            if ticket == 0:
                print("No parking available for", vehicle_type)
            elif ticket == -1:
                print("Invalid vehicle type...Pls try again")
            else:
                print("Alloted Parking Spot No is ", ticket)
        elif input_selected == 2:
            vehicle_type = input("Enter vehicle type (car, motorbike, bus): ")
            spot_number = int(input("Enter your parking spot: "))
            exit_time = datetime.datetime.now()
            fare = parking_lot.calculate_fare(spot_number, vehicle_type, exit_time)
            if fare == 0:
                print("spot number is not allocated to any vehicle")
            elif fare == -1:
                print("Invalid vehicle type...Pls try again")
            else:
                print("Total Fare = ", fare)
        elif input_selected == 3:
            vehicle_type = input("Enter vehicle type (car, motorbike, bus): ")
            vehicle_number = input("Enter your vehicle number: ")
            spot_number = parking_lot.get_parking_spot(vehicle_number, vehicle_type)
            if spot_number == 0:
                print("This vehicle is not parked")
            elif spot_number == -1:
                print("Invalid vehicle type...Pls try again")
            else:
                print("Your Parking Spot is ", spot_number)
        
if __name__ == "__main__":
    main()


