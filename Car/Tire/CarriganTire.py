from Tire.tire import Tire

class CarriganTire(Tire):

    def __init__(self, tireWear):
        self.tireWear = [0, 0, 0, 0]

    def needs_service(self):

        for i in self.tireWear:
            if i >= 0.9:
                return True 
        
        return False