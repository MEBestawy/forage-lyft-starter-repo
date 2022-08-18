
from datetime import date

from battery.battery import Battery


class NubbinBattery(Battery):

    __last_service_date: date
    __current_date: date
    
    def __init__(self, last_service_date, current_date):
        self.__last_service_date = last_service_date
        self.__current_date = current_date

    def needs_service(self) -> bool:
        return (self.__current_date.year - self.__last_service_date.year) >= 4