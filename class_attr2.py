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

    # геттер
    @property
    def grade_ave(self):
        return self._grade_ave

    # сеттер
    @grade_ave.setter
    def grade_ave(self, value: float):
        if isinstance(value, (int, float)):
            self._grade_ave = value


st1 = Student(
    'L2KJK34f4rt5HLL6H3GF$U$%H',
    'PT-302a',
    5,
    4.8
)
print(f'{st1._grade_ave = }')
print(f'{st1.grade_ave = }')

st1._grade_ave = 3.5
print(f'{st1._grade_ave = }')
st1.grade_ave = 3.5
print(f'{st1.grade_ave = }')




