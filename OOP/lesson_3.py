class Point:
    def __init__(self, x=0, y=0):
        # Приватні атрибути
        self.__x, self.__y = x, y

    
    def __checkValue(x):
        return isinstance(x, (int, float))
    
    # Сеттер
    def setCoords(self, x, y):
        # Доповнення його функціоналу, використання закритого методу
        if Point.__checkValue(x) and Point.__checkValue(y):
            self.__x = x
            self.__y = y
        else:
            print("Координати повинні бути числом")
    
    # Геттер
    def getCoords(self):
        return self.__x, self.__y

    
pt = Point(1, 2)
# Помилка при виклику
#print(pt.__x)
# Обхідний шлях
#print(pt._Point__x)


# Операції з публічними даними, здійснені методами get i set
pt.setCoords(10.5, 20)
print(pt.getCoords())
