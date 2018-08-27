class Car:
    def __init__(self,speed,color,name):
        self._speed = speed
        self._color = color
        self._name = name

    def go(self):
        return "Машина {} поехала".format(self._name)

    def stop(self):
        return "Машина {} остановилась".format(self._name)

    def turn(self, direction):
        return "Машина {} повернула {}".format(self._name,direction)

class  TownCar(Car):
    def __init__(self,speed,color,name):
        Car.__init__(self,speed,color,name)
        self._is_police = False

class SportCar(Car):
    def __init__(self,speed,color,name):
        Car.__init__(self,speed,color,name)
        self._is_police = False

class WorkCar(Car):
    def __init__(self,speed,color,name):
        Car.__init__(self,speed,color,name)
        self._is_police = False

class PoliceCar(Car):
    def __init__(self,speed,color,name):
        Car.__init__(self,speed,color,name)
        self._is_police = True

car1 = TownCar(90,"зелёный","Mitsubishi ASX")
print(car1.go())
print(car1.turn("направо"))
print(car1.stop())

car2 = SportCar(150,"Красный","Porsche 911")
print(car2.go())
print(car2.turn("налево"))
print(car2.stop())

car3 = WorkCar(40,"Голубой","ЗИЛ")
print(car3.go())
print(car3.turn("направо"))
print(car3.stop())

car4 = PoliceCar(110,"Белый","BMW 5")
print(car4.go())
print(car4.turn("налево"))
print(car4.stop())
