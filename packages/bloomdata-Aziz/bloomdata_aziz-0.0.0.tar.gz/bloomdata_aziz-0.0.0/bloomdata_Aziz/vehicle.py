'''Returned argument a is squared.'''
class Vehicle:
    '''parent class.'''
    def __init__(self, make, model, color, year, mileage):
        self.make =make
        self.model= model
        self.color=color
        self.year= year
        self.mileage=mileage
    def hank(self):
        ''' define hon function '''
        return 'Hooooonk'
    def drive(self, miles_driven):
        ''' drive func'''
        self.mileage += miles_driven
        return self.mileage
    def __repr__(self) -> str:
        pass
class Convertible(Vehicle):
    '''child class'''
    def __init__(self, make, model, color, year, mileage, top_down = False):
        super().__init__(make, model, color, year, mileage)
        self.top_down= top_down
    def hank(self):
        return 'Hooooonk'
    def drive(self, miles_driven):
        self.mileage += miles_driven
        return self.mileage
    def change_top_status(self):
        ''' func for status'''
        if self.top_down:
            self.top_down =False
            return ' top now is up'
    def __repr__(self) -> str:
        pass




if __name__ == '__main__':
    my_vehicle = Convertible('Toyota', 'Camry', 'Gray', 2015, 60000)
    print(my_vehicle.model)
    print(my_vehicle.drive(90))
    print(my_vehicle.change_top_status())
