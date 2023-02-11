from django.db.models import Model, ForeignKey, ManyToManyField, CASCADE
from django.db.models.fields import CharField, DecimalField, PositiveSmallIntegerField, DateField, BooleanField


class Faculty(Model):
    name = CharField(max_length=100)
    financing = DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'faculties'

    def __str__(self):
        return f'{self.name}'


class Department(Model):
    name = CharField(max_length=100)
    building = PositiveSmallIntegerField()
    financing = DecimalField(max_digits=10, decimal_places=2)
    faculty = ForeignKey(Faculty, CASCADE)

    class Meta:
        db_table = 'departments'

    def __str__(self):
        return f'{self.name}'


class Curator(Model):
    name = CharField(max_length=30)
    surname = CharField(max_length=30)

    class Meta:
        db_table = 'curators'

    def __str__(self):
        return f'{self.name} {self.surname}'


class Teacher(Model):
    name = CharField(max_length=30)
    surname = CharField(max_length=30)
    salary = DecimalField(max_digits=8, decimal_places=2)
    is_professor = BooleanField(default=False)
    subjects = ManyToManyField('Subject', through='Lecture')

    class Meta:
        db_table = 'teachers'

    def __str__(self):
        return f'{self.name} {self.surname}'


class Subject(Model):
    name = CharField(max_length=100)

    class Meta:
        db_table = 'subjects'

    def __str__(self):
        return f'{self.name}'


class Lecture(Model):
    date = DateField()
    teacher = ForeignKey(Teacher, CASCADE)
    subject = ForeignKey(Subject, CASCADE)

    class Meta:
        db_table = 'lectures'

    def __str__(self):
        return f'{self.date:%d.%m.%y} — {self.subject} ({self.teacher})'


class Student(Model):
    name = CharField(max_length=30)
    surname = CharField(max_length=30)
    rating = PositiveSmallIntegerField()

    class Meta:
        db_table = 'students'

    def __str__(self):
        return f'{self.name} {self.surname}'


class Group(Model):
    name = CharField(max_length=10)
    year = PositiveSmallIntegerField()
    department = ForeignKey(Department, CASCADE)
    curators = ManyToManyField(Curator, db_table='groups_curators')
    lectures = ManyToManyField(Lecture, db_table='groups_lectures')
    students = ManyToManyField(Student, db_table='groups_students')

    class Meta:
        db_table = 'groups'

    def __str__(self):
        return f'({self.year}) {self.name}'

