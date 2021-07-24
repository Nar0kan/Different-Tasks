"""
"""

class AMD:
    def __init__(self, *args):
        pass
        #super().__init__(*args)

class Intel:
    def __init__(self, type, *args):
        if type == "Intel":
            self.cpu_type = "Intel"
        else:
            self.cpu_type = "AMD"

class CPU(Intel, AMD):
    def __init__(self, cpu):
        self.cpu = cpu
        #super().__init__(*args)

class NVidia:
    def __init__(self, gpu_type):
        self.gpu_type = gpu_type

class GeForce:
    def __init__(self, *args):
        pass

class GPU(NVidia, GeForce):
    def __init__(self, gpu, *args):
        self.gpu = gpu
        super().__init__(*args)

class Memory:
    def __init__(self, memory):
        self.memory = memory

class Motherboard(CPU, GPU, Memory):
    def __init__(self, cpu, gpu, gpu_type, ram):
        CPU.__init__(self, cpu)
        GPU.__init__(self, gpu, gpu_type)
        Memory.__init__(self, ram)

    def showInfo(self):
        print(self.__dict__)

ex_1 = Motherboard("i3", "MX 130", 'NVidia', 8)
ex_1.showInfo()