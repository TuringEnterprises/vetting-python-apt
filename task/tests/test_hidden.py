import datetime
import unittest

import sys
sys.path.append('.')
sys.path.append('..')

try:
    from src.main import ParkingLot
except:
    from task.src import ParkingLot

class ValidatorTest(unittest.TestCase):

    def test_allocate_parking_car_available(self):
        parking_lot = ParkingLot(1, 0, 0)
        vehicle_number = "ABC123"
        entry_time = datetime.datetime.now()
        spot_number = parking_lot.allocate_parking("car", vehicle_number, entry_time)
        assert spot_number == 1

    def test_allocate_parking_car_unavailable(self):
        parking_lot = ParkingLot(0, 0, 0)
        vehicle_number = "ABC123"
        entry_time = datetime.datetime.now()
        spot_number = parking_lot.allocate_parking("car", vehicle_number, entry_time)
        assert spot_number == 0

    def test_allocate_parking_motorbike_available(self):
        parking_lot = ParkingLot(0, 1, 0)
        vehicle_number = "XYZ456"
        entry_time = datetime.datetime.now()
        spot_number = parking_lot.allocate_parking("motorbike", vehicle_number, entry_time)
        assert spot_number == 1

    def test_allocate_parking_motorbike_unavailable(self):
        parking_lot = ParkingLot(0, 0, 0)
        vehicle_number = "XYZ456"
        entry_time = datetime.datetime.now()
        spot_number = parking_lot.allocate_parking("motorbike", vehicle_number, entry_time)
        assert spot_number == 0

    def test_allocate_parking_bus_available(self):
        parking_lot = ParkingLot(0, 0, 1)
        vehicle_number = "123BUS"
        entry_time = datetime.datetime.now()
        spot_number = parking_lot.allocate_parking("bus", vehicle_number, entry_time)
        assert spot_number == 1

    def test_allocate_parking_bus_unavailable(self):
        parking_lot = ParkingLot(0, 0, 0)
        vehicle_number = "123BUS"
        entry_time = datetime.datetime.now()
        spot_number = parking_lot.allocate_parking("bus", vehicle_number, entry_time)
        assert spot_number == 0

    def test_allocate_parking_invalid_vehicle_type(self):
        parking_lot = ParkingLot(0, 0, 0)
        vehicle_number = "ABC123"
        entry_time = datetime.datetime.now()
        spot_number = parking_lot.allocate_parking("invalid", vehicle_number, entry_time)
        assert spot_number == -1

    def test_calculate_fare_car(self):
        parking_lot = ParkingLot(1, 0, 0)
        vehicle_number = "ABC123"
        entry_time = datetime.datetime.now() - datetime.timedelta(hours=2)
        spot_number = parking_lot.allocate_parking("car", vehicle_number, entry_time)
        exit_time = datetime.datetime.now()
        fare = parking_lot.calculate_fare(spot_number, "car", exit_time)
        assert fare == 60

    def test_calculate_fare_motorbike(self):
        parking_lot = ParkingLot(0, 1, 0)
        vehicle_number = "XYZ456"
        entry_time = datetime.datetime.now() - datetime.timedelta(hours=1)
        spot_number = parking_lot.allocate_parking("motorbike", vehicle_number, entry_time)
        exit_time = datetime.datetime.now()
        fare = parking_lot.calculate_fare(spot_number, "motorbike", exit_time)
        assert fare == 20

    def test_calculate_fare_bus(self):
        parking_lot = ParkingLot(0, 0, 1)
        vehicle_number = "123BUS"
        entry_time = datetime.datetime.now() - datetime.timedelta(hours=3)
        spot_number = parking_lot.allocate_parking("bus", vehicle_number, entry_time)
        exit_time = datetime.datetime.now()
        fare = parking_lot.calculate_fare(spot_number, "bus", exit_time)
        assert fare == 200

    def test_calculate_fare_invalid_vehicle_type(self):
        parking_lot = ParkingLot(0, 0, 0)
        fare = parking_lot.calculate_fare(1, "invalid", datetime.datetime.now())
        assert fare == -1

    def test_calculate_fare_invalid_spot_number(self):
        parking_lot = ParkingLot(1, 0, 0)
        fare = parking_lot.calculate_fare(2, "car", datetime.datetime.now())
        assert fare == 0

    def test_get_parking_spot_car_exists(self):
        parking_lot = ParkingLot(1, 0, 0)
        vehicle_number = "ABC123"
        entry_time = datetime.datetime.now()
        spot_number = parking_lot.allocate_parking("car", vehicle_number, entry_time)
        retrieved_spot_number = parking_lot.get_parking_spot(vehicle_number, "car")
        assert retrieved_spot_number == spot_number

    def test_get_parking_spot_car_not_exists(self):
        parking_lot = ParkingLot(1, 0, 0)
        vehicle_number = "ABC123"
        entry_time = datetime.datetime.now()
        parking_lot.allocate_parking("car", vehicle_number, entry_time)
        retrieved_spot_number = parking_lot.get_parking_spot("XYZ456", "car")
        assert retrieved_spot_number == 0

    def test_get_parking_spot_motorbike_exists(self):
        parking_lot = ParkingLot(0, 1, 0)
        vehicle_number = "XYZ456"
        entry_time = datetime.datetime.now()
        spot_number = parking_lot.allocate_parking("motorbike", vehicle_number, entry_time)
        retrieved_spot_number = parking_lot.get_parking_spot(vehicle_number, "motorbike")
        assert retrieved_spot_number == spot_number

    def test_get_parking_spot_motorbike_not_exists(self):
        parking_lot = ParkingLot(0, 1, 0)
        vehicle_number = "XYZ456"
        entry_time = datetime.datetime.now()
        parking_lot.allocate_parking("motorbike", vehicle_number, entry_time)
        retrieved_spot_number = parking_lot.get_parking_spot("ABC123", "motorbike")
        assert retrieved_spot_number == 0

    def test_get_parking_spot_bus_exists(self):
        parking_lot = ParkingLot(0, 0, 1)
        vehicle_number = "123BUS"
        entry_time = datetime.datetime.now()
        spot_number = parking_lot.allocate_parking("bus", vehicle_number, entry_time)
        retrieved_spot_number = parking_lot.get_parking_spot(vehicle_number, "bus")
        assert retrieved_spot_number == spot_number

    def test_get_parking_spot_bus_not_exists(self):
        parking_lot = ParkingLot(0, 0, 1)
        vehicle_number = "123BUS"
        entry_time = datetime.datetime.now()
        parking_lot.allocate_parking("bus", vehicle_number, entry_time)
        retrieved_spot_number = parking_lot.get_parking_spot("XYZ456", "bus")
        assert retrieved_spot_number == 0

    def test_multiple_cars_allocate_and_exit(self):
        parking_lot = ParkingLot(5, 0, 0)
        vehicles = ["CAR001", "CAR002", "CAR003", "CAR004", "CAR005"]
        entry_times = [datetime.datetime.now(), datetime.datetime.now(), datetime.datetime.now(), datetime.datetime.now(), datetime.datetime.now()]
        spot_numbers = []

        for i in range(len(vehicles)):
            spot_number = parking_lot.allocate_parking("car", vehicles[i], entry_times[i])
            spot_numbers.append(spot_number)

        exit_times = [entry_times[0] + datetime.timedelta(hours=1), entry_times[1] + datetime.timedelta(hours=2),
                    entry_times[2] + datetime.timedelta(hours=3), entry_times[3] + datetime.timedelta(hours=4),
                    entry_times[4] + datetime.timedelta(hours=5)]
        expected_fares = [20, 40, 60, 80, 100]

        for i in range(len(vehicles)):
            fare = parking_lot.calculate_fare(spot_numbers[i], "car", exit_times[i])
            assert fare == expected_fares[i]

    def test_multiple_motorbikes_allocate_and_exit(self):
        parking_lot = ParkingLot(0, 5, 0)
        vehicles = ["XYZ123", "ABC456", "DEF789", "GHI012", "JKL345"]
        entry_times = [datetime.datetime.now(), datetime.datetime.now(), datetime.datetime.now(), datetime.datetime.now(), datetime.datetime.now()]
        spot_numbers = []

        for i in range(len(vehicles)):
            spot_number = parking_lot.allocate_parking("motorbike", vehicles[i], entry_times[i])
            spot_numbers.append(spot_number)

        for i in range(len(vehicles)):
            fare = parking_lot.calculate_fare(spot_numbers[i], "motorbike", datetime.datetime.now())
            assert fare == 10

    def test_multiple_buses_allocate_and_exit(self):
        parking_lot = ParkingLot(0, 0, 5)
        vehicles = ["BUS001", "BUS002", "BUS003", "BUS004", "BUS005"]
        entry_times = [datetime.datetime.now(), datetime.datetime.now(), datetime.datetime.now(), datetime.datetime.now(), datetime.datetime.now()]
        spot_numbers = []

        for i in range(len(vehicles)):
            spot_number = parking_lot.allocate_parking("bus", vehicles[i], entry_times[i])
            spot_numbers.append(spot_number)

        for i in range(len(vehicles)):
            fare = parking_lot.calculate_fare(spot_numbers[i], "bus", datetime.datetime.now())
            assert fare == 50

    def test_allocate_parking_and_exit_sequential(self):
        parking_lot = ParkingLot(1, 1, 1)

        vehicle_numbers = ["CAR001", "MOTOR001", "BUS001"]
        entry_times = [datetime.datetime.now(), datetime.datetime.now(), datetime.datetime.now()]
        exit_times = [entry_times[0] + datetime.timedelta(hours=1), entry_times[1] + datetime.timedelta(hours=2), entry_times[2] + datetime.timedelta(hours=3)]
        spot_numbers = []

        for i in range(len(vehicle_numbers)):
            vehicle_type = "car" if i == 0 else "motorbike" if i == 1 else "bus"
            spot_number = parking_lot.allocate_parking(vehicle_type, vehicle_numbers[i], entry_times[i])
            spot_numbers.append(spot_number)

        for i in range(len(vehicle_numbers)):
            vehicle_type = "car" if i == 0 else "motorbike" if i == 1 else "bus"
            fare = parking_lot.calculate_fare(spot_numbers[i], vehicle_type, exit_times[i])
            assert fare > 0

    def test_allocate_parking_exit_car_motorbike(self):
        parking_lot = ParkingLot(1, 1, 0)
        car_vehicle_number = "ABC123"
        motorbike_vehicle_number = "XYZ456"
        entry_time = datetime.datetime.now()

        car_spot_number = parking_lot.allocate_parking("car", car_vehicle_number, entry_time)
        motorbike_spot_number = parking_lot.allocate_parking("motorbike", motorbike_vehicle_number, entry_time)

        car_exit_time = datetime.datetime.now()
        car_fare = parking_lot.calculate_fare(car_spot_number, "car", car_exit_time)
        assert car_fare == 20

        motorbike_exit_time = datetime.datetime.now()
        motorbike_fare = parking_lot.calculate_fare(motorbike_spot_number, "motorbike", motorbike_exit_time)
        assert motorbike_fare == 10

    def test_allocate_parking_exit_motorbike_bus(self):
        parking_lot = ParkingLot(0, 1, 1)
        motorbike_vehicle_number = "XYZ456"
        bus_vehicle_number = "123BUS"
        entry_time = datetime.datetime.now()

        motorbike_spot_number = parking_lot.allocate_parking("motorbike", motorbike_vehicle_number, entry_time)
        bus_spot_number = parking_lot.allocate_parking("bus", bus_vehicle_number, entry_time)

        motorbike_exit_time = datetime.datetime.now()
        motorbike_fare = parking_lot.calculate_fare(motorbike_spot_number, "motorbike", motorbike_exit_time)
        assert motorbike_fare == 10

        bus_exit_time = datetime.datetime.now()
        bus_fare = parking_lot.calculate_fare(bus_spot_number, "bus", bus_exit_time)
        assert bus_fare == 50

    def test_allocate_parking_exit_bus_car(self):
        parking_lot = ParkingLot(1, 0, 1)
        bus_vehicle_number = "123BUS"
        car_vehicle_number = "ABC123"
        entry_time = datetime.datetime.now()

        bus_spot_number = parking_lot.allocate_parking("bus", bus_vehicle_number, entry_time)
        car_spot_number = parking_lot.allocate_parking("car", car_vehicle_number, entry_time)

        bus_exit_time = datetime.datetime.now()
        bus_fare = parking_lot.calculate_fare(bus_spot_number, "bus", bus_exit_time)
        assert bus_fare == 50

        car_exit_time = datetime.datetime.now()
        car_fare = parking_lot.calculate_fare(car_spot_number, "car", car_exit_time)
        assert car_fare == 20

    def test_allocate_parking_no_capacity(self):
        parking_lot = ParkingLot(0, 0, 0)
        vehicle_number = "ABC123"
        entry_time = datetime.datetime.now()
        spot_number = parking_lot.allocate_parking("car", vehicle_number, entry_time)
        assert spot_number == 0

    def test_calculate_fare_invalid_spot_number_car(self):
        parking_lot = ParkingLot(1, 0, 0)
        fare = parking_lot.calculate_fare(2, "car", datetime.datetime.now())
        assert fare == 0

    def test_calculate_fare_invalid_spot_number_motorbike(self):
        parking_lot = ParkingLot(0, 1, 0)
        fare = parking_lot.calculate_fare(2, "motorbike", datetime.datetime.now())
        assert fare == 0

    def test_calculate_fare_invalid_spot_number_bus(self):
        parking_lot = ParkingLot(0, 0, 1)
        fare = parking_lot.calculate_fare(2, "bus", datetime.datetime.now())
        assert fare == 0

    def test_get_parking_spot_invalid_vehicle_number_car(self):
        parking_lot = ParkingLot(1, 0, 0)
        vehicle_number = "ABC123"
        entry_time = datetime.datetime.now()
        parking_lot.allocate_parking("car", vehicle_number, entry_time)
        retrieved_spot_number = parking_lot.get_parking_spot("XYZ456", "car")
        assert retrieved_spot_number == 0

    def test_get_parking_spot_invalid_vehicle_number_motorbike(self):
        parking_lot = ParkingLot(0, 1, 0)
        vehicle_number = "XYZ456"
        entry_time = datetime.datetime.now()
        parking_lot.allocate_parking("motorbike", vehicle_number, entry_time)
        retrieved_spot_number = parking_lot.get_parking_spot("ABC123", "motorbike")
        assert retrieved_spot_number == 0

    def test_get_parking_spot_invalid_vehicle_number_bus(self):
        parking_lot = ParkingLot(0, 0, 1)
        vehicle_number = "123BUS"
        entry_time = datetime.datetime.now()
        parking_lot.allocate_parking("bus", vehicle_number, entry_time)
        retrieved_spot_number = parking_lot.get_parking_spot("XYZ456", "bus")
        assert retrieved_spot_number == 0

    def test_multiple_cars_allocate_no_capacity(self):
        parking_lot = ParkingLot(2, 0, 0)
        vehicles = ["ABC123", "DEF456", "GHI789"]
        entry_times = [datetime.datetime.now(), datetime.datetime.now(), datetime.datetime.now()]
        spot_numbers = []

        for i in range(len(vehicles)):
            spot_number = parking_lot.allocate_parking("car", vehicles[i], entry_times[i])
            spot_numbers.append(spot_number)

        assert spot_numbers[2] == 0

    def test_multiple_motorbikes_allocate_no_capacity(self):
        parking_lot = ParkingLot(0, 2, 0)
        vehicles = ["XYZ456", "123ABC", "789DEF"]
        entry_times = [datetime.datetime.now(), datetime.datetime.now(), datetime.datetime.now()]
        spot_numbers = []

        for i in range(len(vehicles)):
            spot_number = parking_lot.allocate_parking("motorbike", vehicles[i], entry_times[i])
            spot_numbers.append(spot_number)

        assert spot_numbers[2] == 0

    def test_multiple_buses_allocate_no_capacity(self):
        parking_lot = ParkingLot(0, 0, 2)
        vehicles = ["BUS123", "BUS456", "BUS789"]
        entry_times = [datetime.datetime.now(), datetime.datetime.now(), datetime.datetime.now()]
        spot_numbers = []

        for i in range(len(vehicles)):
            spot_number = parking_lot.allocate_parking("bus", vehicles[i], entry_times[i])
            spot_numbers.append(spot_number)

        assert spot_numbers[2] == 0

    def test_allocate_parking_exit_car_invalid_spot_number(self):
        parking_lot = ParkingLot(1, 0, 0)
        vehicle_number = "ABC123"
        entry_time = datetime.datetime.now()
        spot_number = parking_lot.allocate_parking("car", vehicle_number, entry_time)
        fare = parking_lot.calculate_fare(2, "car", datetime.datetime.now())
        assert fare == 0

    def test_allocate_parking_exit_motorbike_invalid_spot_number(self):
        parking_lot = ParkingLot(0, 1, 0)
        vehicle_number = "XYZ456"
        entry_time = datetime.datetime.now()
        spot_number = parking_lot.allocate_parking("motorbike", vehicle_number, entry_time)
        fare = parking_lot.calculate_fare(2, "motorbike", datetime.datetime.now())
        assert fare == 0

    def test_allocate_parking_exit_bus_invalid_spot_number(self):
        parking_lot = ParkingLot(0, 0, 1)
        vehicle_number = "123BUS"
        entry_time = datetime.datetime.now()
        spot_number = parking_lot.allocate_parking("bus", vehicle_number, entry_time)
        fare = parking_lot.calculate_fare(2, "bus", datetime.datetime.now())
        assert fare == 0

    def test_get_parking_spot_multiple_cars(self):
        parking_lot = ParkingLot(3, 0, 0)
        vehicles = ["ABC123", "DEF456", "GHI789"]
        entry_times = [datetime.datetime.now(), datetime.datetime.now(), datetime.datetime.now()]
        spot_numbers = []

        for i in range(len(vehicles)):
            spot_number = parking_lot.allocate_parking("car", vehicles[i], entry_times[i])
            spot_numbers.append(spot_number)

        retrieved_spot_numbers = []

        for i in range(len(vehicles)):
            retrieved_spot_number = parking_lot.get_parking_spot(vehicles[i], "car")
            retrieved_spot_numbers.append(retrieved_spot_number)

        assert retrieved_spot_numbers == spot_numbers

    def test_get_parking_spot_multiple_motorbikes(self):
        parking_lot = ParkingLot(0, 3, 0)
        vehicles = ["XYZ456", "123ABC", "789DEF"]
        entry_times = [datetime.datetime.now(), datetime.datetime.now(), datetime.datetime.now()]
        spot_numbers = []

        for i in range(len(vehicles)):
            spot_number = parking_lot.allocate_parking("motorbike", vehicles[i], entry_times[i])
            spot_numbers.append(spot_number)

        retrieved_spot_numbers = []

        for i in range(len(vehicles)):
            retrieved_spot_number = parking_lot.get_parking_spot(vehicles[i], "motorbike")
            retrieved_spot_numbers.append(retrieved_spot_number)

        assert retrieved_spot_numbers == spot_numbers

    def test_get_parking_spot_multiple_buses(self):
        parking_lot = ParkingLot(0, 0, 3)
        vehicles = ["BUS123", "BUS456", "BUS789"]
        entry_times = [datetime.datetime.now(), datetime.datetime.now(), datetime.datetime.now()]
        spot_numbers = []

        for i in range(len(vehicles)):
            spot_number = parking_lot.allocate_parking("bus", vehicles[i], entry_times[i])
            spot_numbers.append(spot_number)

        retrieved_spot_numbers = []

        for i in range(len(vehicles)):
            retrieved_spot_number = parking_lot.get_parking_spot(vehicles[i], "bus")
            retrieved_spot_numbers.append(retrieved_spot_number)

        assert retrieved_spot_numbers == spot_numbers

    def test_allocate_parking_exit_car_same_spot_number(self):
        parking_lot = ParkingLot(2, 0, 0)
        vehicle_number1 = "ABC123"
        vehicle_number2 = "ABC456"
        entry_time = datetime.datetime.now()
        spot_number1 = parking_lot.allocate_parking("car", vehicle_number1, entry_time)
        spot_number2 = parking_lot.allocate_parking("car", vehicle_number2, entry_time)
        fare1 = parking_lot.calculate_fare(spot_number1, "car", datetime.datetime.now())
        fare2 = parking_lot.calculate_fare(spot_number2, "car", datetime.datetime.now())
        assert fare1 == fare2

    def test_allocate_parking_exit_motorbike_same_spot_number(self):
        parking_lot = ParkingLot(0, 2, 0)
        vehicle_number1 = "ABC123"
        vehicle_number2 = "ABC456"
        entry_time = datetime.datetime.now()
        spot_number1 = parking_lot.allocate_parking("motorbike", vehicle_number1, entry_time)
        spot_number2 = parking_lot.allocate_parking("motorbike", vehicle_number2, entry_time)
        fare1 = parking_lot.calculate_fare(spot_number1, "motorbike", datetime.datetime.now())
        fare2 = parking_lot.calculate_fare(spot_number2, "motorbike", datetime.datetime.now())
        assert fare1 == fare2

    def test_allocate_parking_exit_bus_same_spot_number(self):
        parking_lot = ParkingLot(0, 0, 2)
        vehicle_number1 = "123BUS"
        vehicle_number2 = "456BUS"
        entry_time = datetime.datetime.now()
        spot_number1 = parking_lot.allocate_parking("bus", vehicle_number1, entry_time)
        spot_number2 = parking_lot.allocate_parking("bus", vehicle_number2, entry_time)
        fare1 = parking_lot.calculate_fare(spot_number1, "bus", datetime.datetime.now())
        fare2 = parking_lot.calculate_fare(spot_number2, "bus", datetime.datetime.now())
        assert fare1 == fare2

    def test_allocate_parking_exit_car_multiple_spots(self):
        parking_lot = ParkingLot(3, 0, 0)
        vehicle_numbers = ["ABC123", "DEF456", "GHI789"]
        entry_times = [datetime.datetime.now(), datetime.datetime.now(), datetime.datetime.now()]
        spot_numbers = []

        for i in range(len(vehicle_numbers)):
            spot_number = parking_lot.allocate_parking("car", vehicle_numbers[i], entry_times[i])
            spot_numbers.append(spot_number)

        fare_total = 0

        for i in range(len(spot_numbers)):
            fare = parking_lot.calculate_fare(spot_numbers[i], "car", datetime.datetime.now())
            fare_total += fare

        assert fare_total == 60

    def test_allocate_parking_exit_motorbike_multiple_spots(self):
        parking_lot = ParkingLot(0, 3, 0)
        vehicle_numbers = ["XYZ456", "123ABC", "789DEF"]
        entry_times = [datetime.datetime.now(), datetime.datetime.now(), datetime.datetime.now()]
        spot_numbers = []

        for i in range(len(vehicle_numbers)):
            spot_number = parking_lot.allocate_parking("motorbike", vehicle_numbers[i], entry_times[i])
            spot_numbers.append(spot_number)

        fare_total = 0

        for i in range(len(spot_numbers)):
            fare = parking_lot.calculate_fare(spot_numbers[i], "motorbike", datetime.datetime.now())
            fare_total += fare

        assert fare_total == 30

    def test_allocate_parking_exit_bus_multiple_spots(self):
        parking_lot = ParkingLot(0, 0, 3)
        vehicle_numbers = ["BUS123", "BUS456", "BUS789"]
        entry_times = [datetime.datetime.now(), datetime.datetime.now(), datetime.datetime.now()]
        spot_numbers = []

        for i in range(len(vehicle_numbers)):
            spot_number = parking_lot.allocate_parking("bus", vehicle_numbers[i], entry_times[i])
            spot_numbers.append(spot_number)

        fare_total = 0

        for i in range(len(spot_numbers)):
            fare = parking_lot.calculate_fare(spot_numbers[i], "bus", datetime.datetime.now())
            fare_total += fare

        assert fare_total == 150


    def test_main(self):
        test_allocate_parking_car_available()
        test_allocate_parking_car_unavailable()
        test_allocate_parking_motorbike_available()
        test_allocate_parking_motorbike_unavailable()
        test_allocate_parking_bus_available()
        test_allocate_parking_bus_unavailable()
        test_allocate_parking_invalid_vehicle_type()
        test_calculate_fare_car()
        test_calculate_fare_motorbike()
        test_calculate_fare_bus()
        test_calculate_fare_invalid_vehicle_type()
        test_calculate_fare_invalid_spot_number()
        test_get_parking_spot_car_exists()
        test_get_parking_spot_car_not_exists()
        test_get_parking_spot_motorbike_exists()
        test_get_parking_spot_motorbike_not_exists()
        test_get_parking_spot_bus_exists()
        test_get_parking_spot_bus_not_exists()
        test_multiple_cars_allocate_and_exit()
        test_multiple_motorbikes_allocate_and_exit()
        test_multiple_buses_allocate_and_exit()
        test_allocate_parking_and_exit_sequential()
        test_allocate_parking_exit_car_motorbike()
        test_allocate_parking_exit_motorbike_bus()
        test_allocate_parking_exit_bus_car()
        test_allocate_parking_no_capacity()
        test_calculate_fare_invalid_spot_number_car()
        test_calculate_fare_invalid_spot_number_motorbike()
        test_calculate_fare_invalid_spot_number_bus()
        test_get_parking_spot_invalid_vehicle_number_car()
        test_get_parking_spot_invalid_vehicle_number_motorbike()
        test_get_parking_spot_invalid_vehicle_number_bus()
        test_multiple_cars_allocate_no_capacity()
        test_multiple_motorbikes_allocate_no_capacity()
        test_multiple_buses_allocate_no_capacity()
        test_allocate_parking_exit_car_invalid_spot_number()
        test_allocate_parking_exit_motorbike_invalid_spot_number()
        test_allocate_parking_exit_bus_invalid_spot_number()
        test_get_parking_spot_multiple_cars()
        test_get_parking_spot_multiple_motorbikes()
        test_allocate_parking_exit_car_same_spot_number()
        test_allocate_parking_exit_motorbike_same_spot_number()
        test_allocate_parking_exit_bus_same_spot_number()
        test_allocate_parking_exit_car_multiple_spots()
        test_allocate_parking_exit_motorbike_multiple_spots()
        test_allocate_parking_exit_bus_multiple_spots()

if __name__ == "__main__":
    test_main()




