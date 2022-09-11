from enum import Enum


class Sex(Enum):
    MALE = 'm'
    FEMALE = 'f'

class Degree(Enum):
    BACHELOR = 'b'
    MASTER = 'm'
    DOCTOR = 'd'


class Person:
    def __init__(self, name: str,
                 birthdate: str,
                 sex: Sex):
        self.__name = name
        self.birthdate = birthdate
        self.sex = sex

    @property
    def name(self):
        return self.__name

class Employee(Person):
    def __init__(self,
                 name: str,
                 birthdate: str,
                 sex: Sex,
                 position: str,
                 salary: int):
        super().__init__(name, birthdate, sex)
        self.position = position
        self.salary = salary


class Researcher(Employee):
    def __init__(self,
                 name: str,
                 birthdate: str,
                 sex: Sex,
                 position: str,
                 salary: int,
                 degree: Degree = Degree.MASTER):
        super().__init__(name, birthdate, sex, position, salary)
        self.degree = degree


class Teacher(Employee):
    def __init__(self,
                 name: str,
                 birthdate: str,
                 sex: Sex,
                 position: str,
                 salary: int,
                 degree: Degree = Degree.MASTER,
                 professorship: bool = False,
                 experience: int = 0):
        super().__init__(name, birthdate, sex, position, salary)
        self.degree = degree
        self.professorship = professorship
        self.experience = experience
        self.__courses: list[str] = []

    def add_course(self, course: str):
        self.__courses.append(course)


t1 = Teacher('Nikolay', '07.08.1972', Sex.MALE, 'laboratory head', 50000)
t1.add_course('Microelectronic')
t1._Teacher__courses.append('Physics')
print(t1._Teacher__courses)




class GeneralPersonnel(Employee):
    pass


p1 = Person('Ivan', '01.06.1980', Sex.MALE)
print(f'{p1.__dict__ = }\n')

e1 = Employee('Ivan', '01.06.1980', Sex.MALE, 'director', None)
print(f'{e1.__dict__ = }\n')

r1 = Researcher('Andrey', '07.08.1972', Sex.MALE, 'laboratory head', 50000, Degree.DOCTOR)
print(f'{r1.__dict__ = }\n')

g1 = GeneralPersonnel('Olga', '08.09.1949', Sex.FEMALE, 'clothkeeper', 10000)
print(f'{g1.__dict__ = }\n')

