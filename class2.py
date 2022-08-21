
class Table:
    def __init__(self):
        """Конструктор, вызываемый во время создания экземпляра."""
        self.legs = 4
        self.width = 100
        self.depth = 80
        self.height = 70


t1, t2 = Table(), Table()
print(t1.__dict__)

t2.legs = 3
t2.width = 50
t2.depth = 50
t2.height = 100
print(t2.__dict__)



class Chair:
    def __init__(self,
                 height: int,
                 width: int,
                 depth: int,
                 office: bool = False):
        self.height = height
        self.width = width
        self.depth = depth
        self.office = office

# Chair.__new__(...) -> self
# Chair.__init__(self, ...)

ch1 = Chair(85, 60, 40)
ch2 = Chair(150, 90, 75, True)
