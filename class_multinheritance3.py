class AppleTree:
    def __init__(self,
                 height: float,
                 apples_in_year: float):
        self.height = height
        self.apples_in_year = apples_in_year


class PearTree:
    def __init__(self,
                 kind: str,
                 height: float,
                 pears_in_year: float):
        self.kind = kind
        self.height = height
        self.pears_in_year = pears_in_year


class WonderTree(AppleTree, PearTree):
    pass

wt1 = WonderTree(4.5, 80.5)


class PeappleTree(AppleTree, PearTree):
    def __init__(self,
                 height: float,
                 fruits_in_year: float,
                 reproductive: bool):
        super().__init__(height, fruits_in_year)
        self.reproductive = reproductive


pa1 = PeappleTree(3.5, 100, False)
print([attr for attr in dir(pa1) if not attr.startswith('__')])

print(pa1.kind)
