"""
Завдання 1. Створити клас Rectangle, в якому є статичний метод, що вичисляє
площу прямокутника. Цей метод приймає два параметра (ширину і довжину),
викликається в ініціалізаторі для вичислення площі конкретного прямокутника і
результат присвоюється локальній змінній створюємого екземпляру класу.
Задвання 2. Створіть клас Dog, у кожному його екземпдярі створіть декілька
локальних змінних (наприклад: кличка, вік та порода) і зробіть так, щоб можна
було створювати не більше пяти екземплярів кдасу.
"""

# Завдання 1
class Rectangle:
    
    @staticmethod
    def find_area(width, height):
        return width * height
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = Rectangle.find_area(width, height)

ex_1 = Rectangle(10, 5)
ex_2 = Rectangle(2, 31)
print(ex_1.__dict__, ex_2.__dict__, sep = '\n')

# Завдання 2
class Dog:
    __count = 0

    def __new__(cls, *args, **kwargs):
        if Dog.__count < 5:
            Dog.__count += 1
            return super(Dog, cls).__new__(cls)
        else:
            print("This is more than 5 doggies")
    
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

dog_1 = Dog("Calculus", 5, "No breed")
dog_2 = Dog("Sauce", 6, "Haskii")
dog_3 = Dog("Miny", 9, "Taksa")
dog_4 = Dog("Pip", 4, "Rotveyler")
dog_5 = Dog("Clutch", 6, "Dogee")
dog_6 = Dog("Cool", 3, "No breed")
print(id(dog_5), id(dog_6))
print(dog_5.name)
#print(dog_6.name) - Raise AttributeError
