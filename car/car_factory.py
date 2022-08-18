
from datetime import date
from battery.models.nubbin_battery import NubbinBattery
from battery.models.spindler_battery import SpindlerBattery

from car.car import Car
from engine.models.capulet_engine import CapuletEngine
from engine.models.sternman_engine import SternmanEngine
from engine.models.willoughby_engine import WilloughbyEngine

class CarFactory:
    @staticmethod
    def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        return Car(
            CapuletEngine(current_mileage, last_service_mileage),
            SpindlerBattery(last_service_date, current_date)
        )
        
    @staticmethod
    def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        return Car(
            WilloughbyEngine(current_mileage, last_service_mileage),
            SpindlerBattery(last_service_date, current_date)
        )

    @staticmethod
    def create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool) -> Car:
        return Car(
            SternmanEngine(warning_light_on),
            SpindlerBattery(last_service_date, current_date)
        )
    
    @staticmethod
    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        return Car(
            WilloughbyEngine(current_mileage, last_service_mileage),
            NubbinBattery(last_service_date, current_date)
        )
    
    @staticmethod
    def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        return Car(
            CapuletEngine(current_mileage, last_service_mileage),
            NubbinBattery(last_service_date, current_date)
        )
