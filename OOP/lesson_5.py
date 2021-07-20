class Point:
    __count = 0

    """ Створення "Сінглтона"
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls.__instance, cls):
            cls.__instance = super(Point, cls).__new__(cls)
        else:
            print("кземпляр класу уже було створено.")
    """
    def __init__(self, x=0, y=0):
        Point.__count += 1
        self.coordX = x
        self.coordY = y

    @staticmethod
    def getCount():
        return Point.__count
    
pt = Point(1, 2)
pt2 = Point(0, 2)
print(pt.getCount())
