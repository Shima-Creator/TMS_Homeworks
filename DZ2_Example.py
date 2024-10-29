#2 Задание
class Car:
    def __init__(self, brand, model, release_year, speed=0):
        self.__brand = brand
        self.__model = model
        self.__release_year = release_year
        self.__speed = speed

    def speed_up(self):
        return self.__speed + 5

    def speed_down(self):
        return self.__speed - 5

    def stop(self):
        self.__speed = 0
        return self.__speed

    def turn(self):
        return self.__speed - (self.__speed * 2)

    def show_speed(self):
        return f"Скорость равна {self.__speed} км/ч"




    #Геттеры
    @property
    def brand(self):
        return self.__brand

    @property
    def model(self):
        return self.__model

    @property
    def release_year(self):
        return self.__release_year

    @property
    def speed(self):
        return self.__speed


 #Cеттеры
    @brand.setter
    def brand(self, car_brand):
        if car_brand:
            self.__brand = car_brand
        else:
            raise ValueError("Choose brand of your car")

    @model.setter
    def model(self, car_model):
        if car_model:
            self.__model = car_model
        else:
            raise ValueError("Choose model of your car")
    @release_year.setter
    def release_year(self, car_release):
        if car_release:
            self.__release_year = car_release
        else:
            raise ValueError("Choose release year of your car")
    @speed.setter
    def speed(self, car_speed):
        if car_speed:
            self.__speed = car_speed
        else:
            raise ValueError("Choose speed of your car")



brand = str(input("Введите марку автомобиля:"))
model = str(input("Введите модель автомобиля:"))
release_year = str(input("Введите год выпуска автомобиля:"))
speed = int(input("Введите скорость автомобиля:"))

your_car = Car(brand, model, release_year, speed)

print(f"Скорость автомобиля {your_car.show_speed()}")
print(f"Скорость автомобиля после увеличения {your_car.speed_up()}")
print(f"Скорость автомобиля после уменьшения {your_car.speed_down()}")
print(f"Скорость автомобиля после разворота {your_car.turn()}")
print(f"Скорость автомобиля после остановки {your_car.stop()}")
