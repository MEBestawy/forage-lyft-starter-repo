
from engine.engine import Engine


class CapuletEngine(Engine):

    __current_mileage: int
    __last_service_mileage: int

    def __init__(self, current_mileage: int, last_service_mileage: int):
        self.__current_mileage = current_mileage
        self.__last_service_mileage = last_service_mileage

    def needs_service(self) -> bool:
        return self.__current_mileage - self.__last_service_mileage > 30000