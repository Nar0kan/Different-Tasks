class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __checkValue(x):
        return isinstance(x, (int, float))

    def __getCoordX(self):
        #print("Виклик методу __getCoordX")
        return self.__x, self.__y

    def __setCoordX(self, new_x):
        #print("Виклик методу __setCoordX")
        if Point.__checkValue(new_x):
            self.__x = new_x
        else:
            raise ValueError("Невірний формат даних.")

    def __delCoordX(self):
        #print("Виклик методу __delCoord")
        del self.__x

    CoordX = property(__getCoordX, __setCoordX, __delCoordX)

ptx = Point(10)
ptx.CoordX = 20
x = ptx.CoordX
print(x, ptx.__dict__)
del ptx.CoordX

# Декоратори

class Point_2:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __checkValue(x):
        return isinstance(x, (int, float))

    @property
    def CoordX(self):
        #print("Виклик методу __getCoordX")
        return self.__x, self.__y

    @CoordX.setter
    def CoordX(self, new_x):
        #print("Виклик методу __setCoordX")
        if Point_2.__checkValue(new_x):
            self.__x = new_x
        else:
            raise ValueError("Невірний формат даних.")


    @CoordX.deleter
    def CoordX(self):
        print("Виклик методу __delCoord")
        del self.__x


ptx = Point_2(10)
ptx.CoordX = 77
x = ptx.CoordX
print(x)
del ptx.CoordX

# Дескриптор CoordValue

class CoordValue:
    def __init__(self, name):
        self.__name = name
    
    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        instance.__dict__[self.__name] = value
    

class Points:
    coordX = CoordValue("coordinate X")
    coordY = CoordValue("coordinate Y")
    
    
    def __init__(self, x=0, y=0):
        self.coordX = x
        self.coordY = y



ptx = Points(10, 2)
ptx.coordX = 5
print(ptx.coordX, ptx.coordY)

pt_2 = Points(222, 0.002)
print(pt_2.coordX, pt_2.coordY)

print(ptx.__dict__, pt_2.__dict__, sep = '\n')
