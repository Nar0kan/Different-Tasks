class Point:
    x,y = 1, 1
    def setCoords(self, x, y):
        self.x = x
        self.y = y

pt = Point()
#pt.x = 5
#pt.y = 10
#Point.setCoord(pt, 5, 10)
pt.setCoords(5, 10)
print(pt.__dict__)


# __init__ конструктор __del__ деструктор
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        #print("Був створенний екземпляр класу Point")
        
    x,y = 1, 1
    def setCoords(self, x, y):
        self.x = x
        self.y = y
    def __del__(self):
        print("Видалення екземпляра: " + self.__str__())

pt = Point(20, 20)
pt2 = Point(10)
pt3 = Point()
print(pt.__dict__)
print(pt2.__dict__)
print(pt3.__dict__)

pt, pt2, pt3 = 0, 0, 0
