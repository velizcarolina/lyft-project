from abc import ABC, abstractclassmethod
from datetime import date
from Car import Car
from Battery.NubbinBattery import NubbinBattery
from Battery.SpindlerBattery import SpindlerBattery
from CapuletEngine import CapuletEngine
from SternmanEngine import SternmanEngine
from WilloughbyEngine import WilloughbyEngine

class CarFactory:

    def factory_method(self):
        pass

    def __init__():
        return

    #Capulet, Splinder
    def create_calliope(current_date:date, last_service_date:date, current_milage:int, last_service_milage:int):
        engine = CapuletEngine(last_service_milage, current_milage)
        battery = SpindlerBattery(last_service_date, current_date)
        car = Car(engine, battery)
        return car
    
    #Willoughby, Splinder
    def create_glissade(current_date:date, last_service_date:date, current_milage:int, last_service_milage:int):
        engine = WilloughbyEngine(last_service_milage, current_milage)
        battery = SpindlerBattery(last_service_date, current_date)
        car = Car(engine, battery)
        return car
    
    #Sternman, Splinder
    def create_palindrome(current_date:date, last_service_date:date, warning_light_on:bool):
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date, current_date)
        car = Car(engine, battery)
        return car
    
    #Willoughby, Nubbin
    def create_rorschach(current_date:date, last_service_date:date, current_milage:int, last_service_milage:int):
        engine = WilloughbyEngine(last_service_milage, current_milage)
        battery = NubbinBattery(last_service_date, current_date)
        car = Car(engine, battery)
        return car
    
    #Capulet, Nubbin
    def create_thovax(current_date:date, last_service_date:date, current_milage:int, last_service_milage:int):
        engine = CapuletEngine(last_service_milage, current_milage)
        battery = NubbinBattery(last_service_date, current_date)
        car = Car(engine, battery)
        return car