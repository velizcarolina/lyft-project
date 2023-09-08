from battery import Battery
from datetime import date


class NubbinBattery(Battery):

    def __init__(self, last_service_date:date, current_date: date):
        self._lastservice_date = last_service_date
        self._current_date = current_date

    
    def needs_service(self):

        if((self._current_date.year - self._lastservice_date.year) >= 2):
            if((self._current_date.month > self._lastservice_date.month)):
                if((self._current_date.day > self._lastservice_date.day)):
                    return True

        return False 