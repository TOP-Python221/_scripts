class Student:
    def __init__(self,
                 student_id: str,
                 group: str,
                 year: int,
                 grade_ave: float):
        self.__id = student_id
        self.group = group
        self.year = year
        self._grade_ave = grade_ave

    def update_grade_ave(self, value: float):
        self._grade_ave = value

    def load_from_db(self):
        # ... self.__id ...
        pass

    def update_in_db(self):
        # ... self.__id ...
        pass


st1 = Student(
    '34l5sd09vwo34tr5w',
    'PT-301',
    4,
    4.4
)
print(f'\nпространство имён:\n{st1.__dict__ = }')
scope = [name for name in dir(st1) if not name.startswith('__')]
print(f'\nобласть видимости:\n{scope = }\n')

st1.update_grade_ave(4.5)
print(f'\nпространство имён:\n{st1.__dict__ = }')

