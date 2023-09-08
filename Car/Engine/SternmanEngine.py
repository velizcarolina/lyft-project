from abc import ABC, abstractclassmethod
from engine import Engine

class SternmanEngine(Engine):

    def __init__(self, warning_light_on: bool):
        self._warning_light_on = warning_light_on

    def needs_service(self):
        return self._warning_light_on