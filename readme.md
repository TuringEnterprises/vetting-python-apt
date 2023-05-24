Problem Statement:

Design a parking lot management system that allows users to allocate parking spaces and calculate fares. The system should support different types of vehicles, including cars, motorbikes, and buses. Implement the following functionalities:

## Task 1

- Allocate Parking:
   Implement a method `allocate_parking` in the `ParkingLot` class that takes the vehicle type, vehicle number, and entry time as input. The method should allocate a parking space for the vehicle based on its type and return the assigned spot number. If no parking space is available for the given vehicle type, return 0 and If the vehicle type is invalid, return -1 Ensure that the allocation process is efficient and avoids duplicate assignments.

## Task 2
- Calculate Fare:
   Implement a method `calculate_fare` in the `ParkingLot` class that takes the spot number, vehicle type, and exit time as input. The method should calculate the fare for the parked vehicle based on the parking rate per hour for the corresponding vehicle type. If the spot number is invalid or the vehicle is not parked in that spot, return 0 and If the vehicle type is invalid, return -1. Ensure that the fare calculation is accurate by using appropriate methods or libraries for duration calculation.

## Task 3
- Get Parking Spot:
   Find the mistakes and correct them in the method `get_parking_spot` in the `ParkingLot` class that takes the vehicle number and vehicle type as input and returns the spot number where the vehicle is parked. If the vehicle number in not parked, return 0 and If the vehicle type is invalid, return -1. Optimise the method to efficiently retrieve the spot number.

Write a complete program that includes the above class definitions and functions to simulate the parking lot system. The program should provide a user interface with the following options:

- Option 1: Allocate Parking
   - Prompt the user to enter the vehicle type (car, motorbike, bus).
   - Prompt the user to enter the vehicle number.
   - Record the entry time.
   - Allocate a parking space for the vehicle and display the assigned spot number.
   - If no parking space is available for the given vehicle type, display an appropriate message.

- Option 2: Exit Parking
   - Prompt the user to enter the vehicle type (car, motorbike, bus).
   - Prompt the user to enter the parking spot number.
   - Record the exit time.
   - Calculate the fare for the parked vehicle based on the exit time and display it.
   - If the spot number is invalid or the vehicle is not parked in that spot, display an appropriate message.

Ensure that the program handles user input validation and error handling for all scenarios, such as invalid vehicle types, invalid spot numbers, and incorrect option selections.

Example Scenarios:

1. Allocate Parking:
   Select mode: Allocate Parking [1], Exit Parking [2], Get Parking Details [3]: 1
   Enter vehicle type (car, motorbike, bus): car
   Enter vehicle number: ABC123
   Allotted Parking Spot No is 5

2. Exit Parking:
   Select mode: Allocate Parking [1], Exit Parking [2], Get Parking Details [3]: 2
   Enter vehicle type (car, motorbike, bus): car
   Enter your parking spot: 5
   Total Fare = 40

3. Exit Parking (Invalid Spot Number):
   Select mode: Allocate Parking [1], Exit Parking [2], Get Parking Details [3]: 3
   Enter vehicle type (car, motorbike, bus): motorbike
   Enter your vehicle number: XYZ789
   Your Parking Spot is 7