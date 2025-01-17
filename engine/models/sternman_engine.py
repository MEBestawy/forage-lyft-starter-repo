
from engine.engine import Engine

class SternmanEngine(Engine):

    __warning_light_is_on: bool

    def __init__(self, warning_light_is_on: bool):
        self.__warning_light_is_on = warning_light_is_on

    def needs_service(self) -> bool:
        return self.__warning_light_is_on