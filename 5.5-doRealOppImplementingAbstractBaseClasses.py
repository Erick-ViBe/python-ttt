from abc import ABC, abstractmethod


class Car(ABC):

    def go(self):
        print("Vroooooom!")

    @abstractmethod
    def speed(self):
        pass


class GenericCar(Car):

    # if you don't create this method, it gives error
    def speed(self):
        print("70mph")


car1 = GenericCar()


class FasCar(Car):
    def speed(self):
        print("100mph")


car2 = FasCar()
