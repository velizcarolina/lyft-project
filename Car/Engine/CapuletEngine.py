from abc import ABC, abstractclassmethod
from engine import Engine

class CapuletEngine(Engine):

    def __init__(self, last_service_mileage:int, current_mileage:int):
        self._last_service_mileage = last_service_mileage
        self._current_mileage = current_mileage

    #needs service every 30k miles
    def needs_service(self):
        return (self._current_mileage - self._last_service_mileage) >= 30000