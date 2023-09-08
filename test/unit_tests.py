import unittest

from datetime import date

from Car import Car
from CarFactory import CarFactory
from Battery.NubbinBattery import NubbinBattery
from Battery.SpindlerBattery import SpindlerBattery
from Engine.CapuletEngine import CapuletEngine
from Engine.SternmanEngine import SternmanEngine
from Engine.WilloughbyEngine import WilloughbyEngine

class TestCalliope(unittest.TestCase):
#Capulet, Splinder
    
    def test_battery_should_be_serviced(self):

        today = date.today()
        last_service_date = today.replace(year=today.year - 4)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_calliope(today, last_service_date, current_mileage, last_service_mileage)

        self.assertTrue(car.needs_service())

  
    def test_battery_should_not_be_serviced(self):
        today = date.today()
        last_service_date = today.replace(month = 8)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_calliope(today, last_service_date, current_mileage, last_service_mileage)

        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = date.today()
        last_service_date = date.today()
        current_mileage = 31000
        last_service_mileage = 0

        car = CarFactory.create_calliope(today, last_service_date, current_mileage, last_service_mileage)

        self.assertTrue(car.needs_service())


    def test_engine_should_not_be_serviced(self):
        today = date.today()
        last_service_date = date.today()
        current_mileage = 90
        last_service_mileage = 0

        car = CarFactory.create_calliope(today, last_service_date, current_mileage, last_service_mileage)

        self.assertFalse(car.needs_service())

class TestGlissade(unittest.TestCase):
#Willoughby, Splinder
    
    def test_battery_should_be_serviced(self):

        today = date.today()
        last_service_date = today.replace(year=today.year - 6)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_glissade(today, last_service_date, current_mileage, last_service_mileage)

        self.assertTrue(car.needs_service())

  
    def test_battery_should_not_be_serviced(self):
        today = date.today()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_glissade(today, last_service_date, current_mileage, last_service_mileage)

        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = date.today()
        last_service_date = date.today()
        current_mileage = 61000
        last_service_mileage = 0

        car = CarFactory.create_glissade(today, last_service_date, current_mileage, last_service_mileage)

        self.assertTrue(car.needs_service())


    def test_engine_should_not_be_serviced(self):
        today = date.today()
        last_service_date = date.today()
        current_mileage = 90
        last_service_mileage = 0

        car = CarFactory.create_glissade(today, last_service_date, current_mileage, last_service_mileage)

        self.assertFalse(car.needs_service())

class TestPalindrome(unittest.TestCase):
#Sternman, Splinder
    
    def test_battery_should_be_serviced(self):

        today = date.today()
        last_service_date = today.replace(year = 4)
        warning_light_on = False

        car = CarFactory.create_palindrome(today, last_service_date, warning_light_on)

        self.assertTrue(car.needs_service())
    
    def test_battery_should_not_be_serviced(self):
        today = date.today()
        last_service_date = today.replace(day = today.day + 1, year = today.year - 4)
        warning_light_on = False

        car = CarFactory.create_palindrome(today, last_service_date, warning_light_on)

        self.assertFalse(car.needs_service())

    
    def test_engine_should_be_serviced(self):
        today = date.today()
        last_service_date = today
        warning_light_on = True

        car = CarFactory.create_palindrome(today, last_service_date, warning_light_on)

        self.assertTrue(car.needs_service())


    def test_engine_should_not_be_serviced(self):
        today = date.today()
        last_service_date = today
        warning_light_on = False

        car = CarFactory.create_palindrome(today, last_service_date, warning_light_on)
        
        self.assertFalse(car.needs_service())

class TestRorschach(unittest.TestCase):
#Willoughby, Nubbin
    
    def test_battery_should_be_serviced(self):

        today = date.today()
        last_service_date = today.replace(year=today.year - 2)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_rorschach(today, last_service_date, current_mileage, last_service_mileage)

        self.assertTrue(car.needs_service())

  
    def test_battery_should_not_be_serviced(self):
        today = date.today()
        last_service_date = today.replace(month = today.month + 1)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_rorschach(today, last_service_date, current_mileage, last_service_mileage)

        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = date.today()
        last_service_date = date.today()
        current_mileage = 60000
        last_service_mileage = 0

        car = CarFactory.create_rorschach(today, last_service_date, current_mileage, last_service_mileage)

        self.assertTrue(car.needs_service())


    def test_engine_should_not_be_serviced(self):
        today = date.today()
        last_service_date = date.today()
        current_mileage = 59999
        last_service_mileage = 0

        car = CarFactory.create_rorschach(today, last_service_date, current_mileage, last_service_mileage)

        self.assertFalse(car.needs_service())

class TestThovax(unittest.TestCase):
#Capulet, Nubbin
     
    def test_battery_should_be_serviced(self):

        today = date.today()
        last_service_date = today.replace(month = today.month - 1, year = today.year - 2)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_thovax(today, last_service_date, current_mileage, last_service_mileage)

        self.assertTrue(car.needs_service())

  
    def test_battery_should_not_be_serviced(self):
        today = date.today()
        last_service_date = today.replace(day = today.day + 1, year = today.year - 2)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_thovax(today, last_service_date, current_mileage, last_service_mileage)

        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = date.today()
        last_service_date = date.today()
        current_mileage = 30000.1
        last_service_mileage = 0

        car = CarFactory.create_thovax(today, last_service_date, current_mileage, last_service_mileage)

        self.assertTrue(car.needs_service())


    def test_engine_should_not_be_serviced(self):
        today = date.today()
        last_service_date = date.today()
        current_mileage = 2
        last_service_mileage = 0

        car = CarFactory.create_thovax(today, last_service_date, current_mileage, last_service_mileage)

        self.assertFalse(car.needs_service())



if __name__ == '__main__':
    unittest.main()