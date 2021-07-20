'''
Завдання 1. Викликати клас Calendar для збереження дати: день, місяць, рік.
Визначити налаштування для запису і зчитування цієї інформації з цього класу.
(Доповнення: використовуючи __slots__ дозвольте використовувати лише визначені
локальні налаштування в екземплярах класу).
Завдання 2. Створіть клас Rectangle, зберігающий координати: верхньої лівої -
ul та правої нижньої - dr точок. Створіть дескриптори для запису і
зчитування цих значень в класі (атрибути з даними координат повинні
бути приватними).
'''

# Завдання 1
class Calendar:
    __slots__ = ['day', 'month', 'year']
    
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        
    def getdate(self):
        return self.day, self.month, self.year

    def setdate(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    
example_1 = Calendar(10, 3, 2021)
example_1.day = 20
print(example_1.getdate())


# Завдання 2
class Descriptor:
    def __init__(self, name):
        self.__name = name
        
    def __set__(self, instance, value):
        instance.__dict__[self.__name] = value
            
    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]
    

class Rectangle:
    ul = Descriptor("ul")
    dr = Descriptor("dr")
    
    def __init__(self, ul = (0, 0), dr = (0, 0)):
        self.ul = ul
        self.dr = dr
    
example_2 = Rectangle((2, 10), (0, 20))
#example_2.dr = (-1, 30)
#example_2.ul = (0, 1)
print(example_2.ul, example_2.dr)
