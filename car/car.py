from abc import ABC, abstractmethod

from battery.battery import Battery
from engine.engine import Engine
from utils.serviceable import Serviceable

class Car(Serviceable):

    __engine: Engine
    __battery: Battery

    def __init__(self, engine: Engine, battery: Battery):
        self.__engine = engine
        self.__battery = battery

    @abstractmethod
    def needs_service(self) -> bool:
        pass
