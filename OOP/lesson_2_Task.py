"""
1. Створіть клас Point3D, який зберігає координати у вигляді списку. Пропишіть
у ньому конструктор для створення екземплярів з локальними координатами.
Також додайте методи, що дозволяють змінювати координати і отримувати їх
(у вигляді кортежу).
2. Оголосіть клас Point з конструктором, який дозволив би створювати
екземпляр на основі іншого, вже існуючого. Якщо аргументи в конструктор не
передаються, то створюється обєкт з локальними атрибутами за завмовчанням.
3. Напишіть програму, в якій користувач уводить координати  з клавіатури,
створюється відповідний екземпляр і він зберігається в списку. Кількість
введених обєктів N=5. Потім вивести їх атрибути в консоль.
"""

# 1 Завдання
print("\n Завдання 1")
class Point3D:
    xyz = [0, 0, 0]
    def __init__(self, x=0, y=0, z=0):
        self.xyz = [x, y, z]
    def getCoords(self):
        return tuple(self.xyz)
    def setCoords(self, x, y, z):
        self.xyz = [x, y, z]

pt1 = Point3D(10, -2, 3)
print(pt1.__dict__)
print(pt1.getCoords())
pt1.setCoords(-1, -1, -1)
print(pt1.getCoords())

# 2 Завдання
print("\n Завдання 2")
class Point:
    def __init__(self, model = None, x=0, y=0):
        if model:
            self.x = model.x
            self.y = model.y
        else:
            self.x = x
            self.y = y

pt_model = Point(None, 2, 3)
print(pt_model.__dict__)
pt2 = Point(pt_model)
print(pt2.__dict__)

# 3 Завдання
print("\n Завдання 3")
class Points:
    spisok = []
    def __init__(self, x = 0, y = 0):
        Points.spisok.append((x, y))

for N in range(5):
    x = int(input("Input x: "))
    y = int(input("Input y: "))
    ex = Points(x, y)
print(Points.spisok)
