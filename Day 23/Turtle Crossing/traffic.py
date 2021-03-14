from car import Car


class Traffic:
    def __init__(self, turtle):
        self.cars = []
        self.turtle = turtle
        self.generateCars()

    def generateCars(self):
        for _ in range(10):
            car = Car()
            self.cars.append(car)

    def driveCars(self):
        for i, car in enumerate(self.cars):
            if car.distance(self.turtle) < 20:
                return "crash"
            if car.xcor() < -320:
                newCar = Car()
                newCar.speed = car.speed
                self.cars[i] = newCar
            car.drive()

    def increase_speed(self):
        for car in self.cars:
            car.speed += 5
