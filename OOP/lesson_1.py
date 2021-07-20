class Point:
    "Клас для представлення координат точок на площині"
    x = 1
    y = 1

#print(Point.__doc__)
#print(Point.__name__)
#print(dir(Point))

pt = Point()
# Перевірка приналежності pt до класу Point
print(isinstance(pt, Point))
# Виведення локальних змінних об'єкту pt
print(pt.__dict__)

# Зміна значення атрибута х класа Point
Point.x = 100
print(pt.x, pt.y)

# Зміна локальних змінних екземпляра класа pt.
pt.x = 5
pt.y = 10
print(pt.x, Point.x)
print(pt.__dict__)

"""Використання методів атрибутів:"""

#Доставання атрибуту
print(getattr(pt, 'x'))

#Третє значення буде повертатись, якщо атрибута не існує
print(getattr(pt, 'z', False))

print(hasattr(pt, 'y'))

#Створення нового атрибуту та його видалення
setattr(pt, 'z', 20)
print(pt.__dict__)
delattr(pt, "z")
print(hasattr(pt, "z"))
