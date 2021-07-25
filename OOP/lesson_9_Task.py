"""
Завдання 1. Написати клас Point_3D для збереження координат в трьохвимірному просторі (x,y,z). 
Реалізувати перегрузку операторів додавання, віднімання, множення і ділення для цього класу.
Також створити можливість порівнювати координати між собою і записувати/зчитувати значення
через ключі "x", "y", "z".
"""

# Завдання 1
class Point_3D:
    def __init__(self, x, y, z):
        self.__x = x
        self.__y = y
        self.__z = z
        Point_3D.__checkCoords(self)

    def getCoord(self, coord = "all coords"):
        if coord == 'x':
            return self.__x
        elif coord == 'y':
            return self.__y
        elif coord == 'z':
            return self.__z
        else:
            return self.__x, self.__y, self.__z


    def __checkCoords(other):
        if not isinstance(other.getCoord('x'), (float, int)) or \
            not isinstance(other.getCoord('y'), (float, int)) or \
            not isinstance(other.getCoord('z'), (float, int)):
                raise ValueError("Значення координат повинні бути числами!")
    
    # operations
    def __add__(self, other):
        Point_3D.__checkCoords(other)

        x = self.__x + other.getCoord('x')
        y = self.__y + other.getCoord('y')
        z = self.__z + other.getCoord('z')

        return Point_3D(x, y, z)

    def __iadd__(self, other):
        Point_3D.__checkCoords(other)

        self.__x = self.__x + other.getCoord('x')
        self.__y = self.__y + other.getCoord('y')
        self.__z = self.__z + other.getCoord('z')

        return self
    
    def __sub__(self, other):
        Point_3D.__checkCoords(other)

        x = self.__x - other.getCoord('x')
        y = self.__y - other.getCoord('y')
        z = self.__z - other.getCoord('z')

        return Point_3D(x, y, z)

    def __mul__(self, other):
        Point_3D.__checkCoords(other)

        x = self.__x * other.getCoord('x')
        y = self.__y * other.getCoord('y')
        z = self.__z * other.getCoord('z')

        return Point_3D(x, y, z)

    def __truediv__(self, other):
        Point_3D.__checkCoords(other)

        x = self.__x / other.getCoord('x')
        y = self.__y / other.getCoord('y')
        z = self.__z / other.getCoord('z')

        return Point_3D(x, y, z)

    # compare
    def __eq__(self, other):
        Point_3D.__checkCoords(other)

        if self.__x == other.getCoord('x') and \
            self.__y == other.getCoord('y') and \
            self.__z == other.getCoord('z'):
                return True
        return False

    def __nq__(self, other):
        return not Point_3D.__eq__(self, other)

    # get values and set them by keys
    def __getitem__(self, item):
        if not isinstance(item, str):
            raise ValueError("Ключ повинен бути str типу!")

        if item.lower() == 'x':
            return self.__x
        elif item.lower() == 'y':
            return self.__y
        elif item.lower() == 'z':
            return self.__z
        else:
            return "Немає атрибуту " + item + " у екземплярі даного класу."

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise ValueError("Ключ повинен бути str типу.")
        if not isinstance(value, (int, float)):
            raise ValueError("Присвоювати значення координатам необхідно лише числовим типом")

        if key.lower() == 'x':
            self.__x = value
        elif key.lower() == 'y':
            self.__y = value
        elif key.lower() == 'z':
            self.__z = value
        else:
            return "Немає атрибуту " + key + " у екземплярі даного класу."


def test_one():
    ex_1 = Point_3D(10, 20, 30)
    ex_2 = Point_3D(1, 2, 3)

    # add, substract, multiply and divide
    print("\nOperations: ")
    ex_3 = ex_1 + ex_2
    print(ex_3.getCoord())
    ex_3 = ex_2 - ex_1
    print(ex_3.getCoord())
    ex_3 = ex_2 * ex_1
    print(ex_3.getCoord())
    ex_3 = ex_1 / ex_2
    print(ex_3.getCoord())

    # iadd
    ex_1 += ex_2
    print(ex_1.getCoord(), '\n')

    # equality compare
    print("\nEquality compare: ")
    print(ex_1 == ex_3)
    print(ex_1 != ex_2, '\n')

    # __getitem__
    print("__getitem__ and __setitem__ methods on ex_2: ")
    print(ex_2['x'], ex_2['y'], ex_2['z'])
    print(ex_2['x'] > ex_2['y'], end = '\n')

    # __setitem__
    ex_2['X'], ex_2['y'], ex_2['Z'] = 0, 0, 0
    print(ex_2.getCoord())


if __name__ == "__main__":
    test_one()