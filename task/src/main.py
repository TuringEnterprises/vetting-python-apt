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
        if vehicle_type == "car":
            if self.car_spaces > 0:
                self.car_spaces -= 1
                i = True
                while(i):
                    random_spot = random.randint(1, self.max_car_spaces)
                    if(random_spot not in self.car_capacity.keys()):
                        self.car_capacity[random_spot] = vehicle_number,entry_time
                        i = False
                return random_spot
            return 0
        elif vehicle_type == "bus":
            if self.bus_spaces > 0:
                self.bus_spaces -= 1
                i = True
                while(i):
                    random_spot = random.randint(1, self.max_bus_spaces)
                    if(random_spot not in self.bus_capacity.keys()):
                        self.bus_capacity[random_spot] = vehicle_number,entry_time
                        i = False
                return random_spot
            return 0
        elif vehicle_type == "motorbike":
            if self.motorbike_spaces > 0:
                self.motorbike_spaces -= 1
                i = True
                while(i):
                    random_spot = random.randint(1, self.max_motorbike_spaces)
                    if(random_spot not in self.motorbike_capacity.keys()):
                        self.motorbike_capacity[random_spot] = vehicle_number,entry_time
                        i = False
                return random_spot
            return 0
        else:
            return -1

    def calculate_fare(self, spot_number, vehicle_type, exit_time):
        if vehicle_type == "car":
            if(spot_number not in self.car_capacity.keys()):
                return 0
            entry_time = self.car_capacity[spot_number][1]
            del self.car_capacity[spot_number]
            duration = exit_time - entry_time
            return math.ceil(duration.total_seconds()/3600) * Car().parking_rate
        elif vehicle_type == "bus":
            if(spot_number not in self.bus_capacity.keys()):
                return 0
            entry_time = self.bus_capacity[spot_number][1]
            del self.bus_capacity[spot_number]
            duration = exit_time - entry_time
            return math.ceil(duration.total_seconds()/3600) * Bus().parking_rate
        elif vehicle_type == "motorbike":
            if(spot_number not in self.motorbike_capacity.keys()):
                return 0
            entry_time = self.motorbike_capacity[spot_number][1]
            del self.motorbike_capacity[spot_number]
            duration = exit_time - entry_time
            return math.ceil(duration.total_seconds()/3600) * Motorbike().parking_rate
        else:
            return -1

    def get_parking_spot(self, vehicle_num, vehicle_type):
        if vehicle_type == "car":
            for key in self.car_capacity.keys():
                if vehicle_num == self.car_capacity[key][0]:
                    return key
            return 0
        elif vehicle_type == "bus":
            for key in self.bus_capacity.keys():
                if vehicle_num == self.bus_capacity[key][0]:
                    return key
            return 0
        elif vehicle_type == "motorbike":
            for key in self.motorbike_capacity.keys():
                if vehicle_num == self.motorbike_capacity[key][0]:
                    return key
            return 0
        else:
            return -1


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


