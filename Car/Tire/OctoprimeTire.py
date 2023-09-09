from Tire.tire import Tire

class OctoprimeTire(Tire):

    def __init__(self, tireWear):
        self.tireWear = [0, 0, 0, 0]

    def needs_service(self):

        count = 0 

        for i in self.tireWear:
            count = count + i

        if count >= 3:
            return True
         
        return False