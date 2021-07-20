class Prop:
    def __init__(self, sp:tuple, ep:tuple, color:str = "red", width:int = 1):
        self._sp = sp
        self._ep = ep
        self._color = color
        self._width = width

class Line(Prop):
    def drawLine(self):
        print(f"Креслення лінії:{self._sp}, {self._ep}, {self._color}, {self._width}")
#print(issubclass(Line, object))
#print(issubclass(Line, Prop))


class Rectangle(Prop):
    def __init__(self, *args):
        super().__init__(*args)
    
    def drawRect(self):
        print(f"Креслення прямокутника:{self._sp}, {self._ep}, {self._color}, {self._width}")

ex_1 = Line( (1, 0), (10, 2))
ex_1.drawLine()

ex_2 = Rectangle((0, 0), (2, 2))
ex_2.drawRect()




"""
Taken from metanit.com
"""
class Person:
    def __init__(self, name, age):
        self.__name = name  # задаємо ім'я
        self.__age = age  # задаємо вік
 
    @property
    def age(self):
        return self.__age
 
    @age.setter
    def age(self, age):
        if age in range(1, 120):
            self.__age = age
        else:
            print("Недопустимий вік")
            
    @property
    def name(self):
        return self.__name
 
    def display_info(self):
        print("Ім'я:", self.__name, "\tВік:", self.__age)
 
 
class Employee(Person):

    def __init__(self, company, salary):
        super().__init__(self)
        self.__salary = salary
        self.__company = company
 
    def details(self, company):
        # print(self.__name, "работает в компании", company) # так нельзя, self.__name - приватный атрибут
        print(self.name, "работает в компании", company)
 
 
tom = Employee("Tom", 23, "Google", 2000)
tom.details("Google")
tom.age = 33
tom.display_info()
