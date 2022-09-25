
class Test:
    def param(self):
        print(f'я метод экземпляра {self}')

    @staticmethod
    def pampam():
        print('я статический метод')
    
    @classmethod
    def pompom(cls):
        print(f'я метод объекта класса {cls}')


class ChildTest(Test):
    pass


t1 = Test()

t1.param()
# t1.param() -> Test.param(t1)

t1.pampam()
# t1.pampam() -> Test.pampam()

t1.pompom()
# t1.pampam() -> Test.pampam(Test)


print()

c1 = ChildTest()

c1.param()
# c1.param() -> ChildTest.param(c1)

c1.pampam()
# c1.pampam() -> ChildTest.pampam()

c1.pompom()
# c1.pampam() -> ChildTest.pampam(ChildTest)
