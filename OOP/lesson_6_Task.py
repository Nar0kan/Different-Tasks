# Завдання 1
print("\n\nExample_1: \n")

class PC:
    def __init__(self, RAM, DISK, MODEL, CPU):
        self.ram = RAM
        self.disk = DISK
        self.model = MODEL
        self.cpu = CPU

class Laptop(PC):
    def __init__(self, RAM, DISK, MODEL, CPU, dimensions, diagonal):
        self.dimensions = dimensions
        self.diagonal = diagonal
        super().__init__(RAM, DISK, MODEL, CPU)

    def get_spec(self):
        print(self.dimensions, self.diagonal, sep = ", ")

class DesktopPC(PC):
    def __init__(self, RAM, DISK, MODEL, CPU, monitor, mouse, keyboard, atx):
        self.monitor = monitor
        self.mouse = mouse
        self.keyboard = keyboard
        self.atx = atx
        super().__init__(RAM, DISK, MODEL, CPU)

    def get_spec(self):
        print(self.monitor, self.mouse, self.keyboard, self.atx, sep = ", ")

laptop_1 = Laptop(8, '1TB', 'Acer', 'I3 6006U', 'Average', 15.6)
laptop_1.get_spec()

desktop_1 = DesktopPC(4, "1TB", "HP", "Pentium G4560", "LG",
                      "Hator DeighV2", "Hator Rockfall EVO", "Mini")
desktop_1.get_spec()

