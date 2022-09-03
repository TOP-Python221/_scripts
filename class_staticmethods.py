
class Test:
    def param(self):
        print(f'я метод класса {self.__class__.__name__}')

    @staticmethod
    def pampam():
        print('я статический метод')


class ChildTest(Test):
    pass


t1 = Test()

t1.param()
# t1.param() -> Test.param(t1)

t1.pampam()
# t1.pampam() -> Test.pampam()


c1 = ChildTest()

c1.param()
# c1.param() -> Test.param(c1)

c1.pampam()
# c1.pampam() -> Test.pampam()
