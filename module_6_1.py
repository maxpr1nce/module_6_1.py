class Animal:
    def __init__(self, name):
        self.alive = True  # Живое существо
        self.fed = False   # Накормленное ли
        self.name = name   # Имя животного

class Plant:
    def __init__(self, name, edible=False):
        self.edible = edible  # Съедобное ли растение
        self.name = name      # Имя растения

class Mammal(Animal):
    def eat(self, food):
        if food.edible:
            self.fed = True
            print(f"{self.name} съел {food.name}")
        else:
            self.alive = False
            print(f"{self.name} не стал есть {food.name} и погиб!")

class Predator(Animal):
    def eat(self, food):
        if food.edible:
            self.fed = True
            print(f"{self.name} съел {food.name}")
        else:
            self.alive = False
            print(f"{self.name} не стал есть {food.name} и погиб!")

class Flower(Plant):
    def __init__(self, name):
        super().__init__(name, edible=False)  # Цветы не съедобные

class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name, edible=True)   # Фрукты съедобные

# Создание объектов

# Создаем млекопитающее и хищника
lion = Predator("Лев")
bear = Mammal("Медведь")

# Создаем растения
rose = Flower("Роза")
apple = Fruit("Яблоко")

# Действия
lion.eat(rose)   # Лев пытается съесть розу
bear.eat(apple)  # Медведь пытается съесть яблоко   