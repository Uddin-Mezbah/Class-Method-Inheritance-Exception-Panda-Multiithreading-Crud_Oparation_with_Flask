#instance method
#static method
#class method
#anstrct method

# class School:
#     school_name = 'ABC School' #class variable
#     def __init__(self,name) -> None:
#         self.name = name #instance variable

#     def prntname(self):
#         print(self.name) #instanc methode

#     def get_name(cls):
#         cls.school_name = "abcd scholl"
#         print(cls.name)

    
#     def change_name(self,name):
#         self.school_name = name
        
#     @classmethod
#     def change_school_name(cls):
#         cls.school_name = "abcd scholl"
#     @staticmethod
#     def greet():
#         print("Hello Students")


# s = School('uddin')
# s2 = School('rahat')
# # s.prntname()
# s.change_name('nantong university')
# # School().get_name()
# School.change_school_name()
# print(s2.school_name)
# School.greet()

#abstract class/method
from abc import ABC, abstractmethod
class Vehicale(ABC):
    @abstractmethod
    def go(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class Car(Vehicale):
    def go(self):
        print("I am Car")

    def stop(self):
        print("stop yor car")
    

class MotorBike(Vehicale):
    def go(self):
        print("I am a motor bike")
    def stop(self):
        print("stop yor bik")
    

# c = Vehicale()
# c.go()
# car = Car()
# car.go()
mb = MotorBike()
mb.go()