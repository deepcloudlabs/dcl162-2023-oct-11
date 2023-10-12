"""
Exception           -> base   /super class
OverCapacityError   -> derived/sub   class
"""


class OverCapacityError(Exception):
    def __init__(self, message: str, over_capacity: float):
        super().__init__()
        self.over_capacity = over_capacity


class vehicle(object):
    """
    class -> encapsulation + information hiding principle
    members: i) attribute/state/data -> capacity, current_load, vehicle_id
            ii) method -> dynamic behaviour: __init__ (constructor), load, unload
           iii) property
    """

    def __init__(self, vehicle_id: str, capacity: float = 1_000):
        self.__vehicle_id = vehicle_id
        self.__capacity = capacity
        self.__current_load = 0

    @property
    def capacity(self) -> float:
        return self.__capacity

    @property
    def current_load(self) -> float:
        return self.__current_load

    @property
    def vehicle_id(self) -> str:
        return self.__vehicle_id

    @capacity.setter
    def capacity(self, new_capacity: float) -> None:
        if new_capacity <= 0:
            raise ValueError(f"New capacity ({new_capacity}) must be a positive value.")
        self.__capacity = new_capacity

    def load(self, weight: float) -> float:
        """
        loads some weight to the vehicle
        :param weight: the amount of load in kg
        :return:
        """
        if weight <= 0.0:
            raise ValueError(f"weight ({weight}) must be positive value.")
        if self.__current_load + weight > self.__capacity:
            over_capacity = self.__current_load + weight - self.__capacity
            raise OverCapacityError("Vehicle capacity is exceeded.", over_capacity)
        self.__current_load += weight
        return self.__current_load

    def unload(self, weight: float) -> float:
        if weight <= 0.0:
            raise ValueError(f"weight ({weight}) must be positive value.")
        if weight > self.__current_load:
            raise ValueError(f"weight ({weight}) must be less than or equal to current load ({self.__current_load}).")
        self.__current_load -= weight
        return self.__current_load

    def __str__(self) -> str:
        return f"vehicle(id: {self.vehicle_id}, capacity: {self.capacity}, current load: {self.current_load})"

try:
    vehicle_1 = vehicle("1", 5_000)
    print(str(vehicle_1))
    vehicle_1.capacity = 7_500
    # vehicle_1.current_load += 10_000
    vehicle_1.load(2500)
    print(vehicle_1)
    vehicle_1.load(750)
    print(vehicle_1)
    vehicle_1.load(250)
    print(vehicle_1)
    vehicle_1.load(1500)
    print(vehicle_1)
    vehicle_1.load(1)
    print(vehicle_1)
except ValueError as ve:
    print(ve)
except OverCapacityError as oce:
    print(f"Capacity is exceeded: {oce.over_capacity} kg")
