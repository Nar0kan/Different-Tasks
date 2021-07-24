"""
Завдання 1. Створіть базовий клас Table і дочірні: Rectangle Table, Round Table.
Через ініціалізатор базового класу передавайте розмір поверхні столу: для прямокутного -
ширина і довжина, для круглого - радіус. В дочірніх класах реалізуйте метод
вираховування площі поверхні столу.
Завдання 2. Створіть клас Animal і різні похідні від нього підкласи: Dog, Bird, Fox, Cat і т.п.
Реалізуйте в них спільний метод say(), який би вертав звук, видаваний цією твариною.
Створіть кортеж із декількох цих екземплярів класу, переберіть їх в циклі та виведіть
їх звуки (методом say())
"""

# Завдання 1
class Table:
    def __init__(self, el_1 = None, el_2 = None):
        if el_2:
            self.width = el_1
            self.height = el_2
        else:
            self.radius = el_1

class RectTable(Table):
    def calculate_area(self):
        return str(f"Rectangle-Table area: {self.width * self.height}")

class RoundTable(Table):
    def calculate_area(self):
        from math import pi
        return str(f"Round-Table area: {(self.radius**2)*pi}")

ex_1 = RectTable(10, 20)
print("\n\nExample_1: ")
print(ex_1.calculate_area())
ex_2 = RoundTable(10)
print(ex_2.calculate_area(), end = "\n\n Example 2:\n")


# Завдання 2
class Animal:
    def say(self):
        if self.__class__.__name__ == "Dog":
            print(" Bark! ")
        elif self.__class__.__name__ == "Bird":
            print(" Tweet! ")
        elif self.__class__.__name__ == "Cat":
            print(" Meow! ")
        elif self.__class__.__name__ == "Fox":
            print(" What does the fox say?! ")

class Dog(Animal):
    pass

class Bird(Animal):
    pass

class Fox(Animal):
    pass

class Cat(Animal):
    pass

ex_1 = Dog()
ex_2 = Bird()
ex_3 = Fox()
ex_4 = Cat()

kort = (ex_1, ex_2, ex_3, ex_4)
for el in kort:
    el.say()