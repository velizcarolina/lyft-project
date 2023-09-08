from abc import ABC, abstractmethod
from Engine import engine
from Battery import battery
from typing import List
import Serviceable

class Car(Serviceable):
    #constructor
    def __init__(self, engine: engine, battery: battery):
        self._engine = engine
        self._battery = battery

    def strategy(self):
        return self._engine
    
    def strategy(self):
        return self._battery

    def needs_service(self):
        return battery.Battery.needs_service(self._battery) or engine.Engine.needs_service(self._engine)
    