class Vehicle:
    info = { }

    def __init__(self, *cargo):
        self.cargo = []
        for item in cargo: self.cargo.append(item)

    def unload(self):
        for item in self.cargo:
            print(item)

    @classmethod
    def print_info(cls):
        print()
        print(f'Info on {cls.__name__}')
        for key, value in cls.info.items():
            print(f'{key}: {value}')

class Airplane(Vehicle):
    info = { 'Capacity': 5, 'Color': 'Red' }
    def unload(self):
        for item in self.cargo:
            print(f'Unloading airplane cargo: {item}')

class Car(Vehicle):
    info = { 'Wheels': 4 }
    def unload(self):
        for item in self.cargo:
            print(f'Unloading car cargo: {item}')

class Boat(Vehicle):
    info = { 'Name': 'Titanic' }
    def unload(self):
        for item in self.cargo:
            print(f'Unloading boat cargo: {item}')

def load_vehicle(cls):
    return cls('crate 1', 'crate 2', 'barrel', 'red carpet', 'canary')



car = load_vehicle(Car)
boat = load_vehicle(Boat)
airplane = load_vehicle(Airplane)

# car.unload()
# boat.unload()
# airplane.unload()

Car.print_info()
Boat.print_info()
Airplane.print_info()
