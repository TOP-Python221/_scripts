from django.urls import path

from faculties.models import Faculty, Department
from faculties.views import MainPage, FacultyView, department_view, contact_view, ProcessStudent

urlpatterns = []

for faculty in Faculty.objects.all():
    urlpatterns += [path(
        f'{faculty.acronym}/',
        FacultyView.as_view(),
        kwargs={'pk': faculty.id},
        name=f'{faculty.acronym}',
    )]

for dep in Department.objects.all():
    urlpatterns += [path(
        f'{dep.faculty.acronym}/{dep.acronym}/',
        department_view,
        kwargs={'pk': dep.id},
        name=f'{dep.faculty.acronym}_{dep.acronym}',
    )]

urlpatterns += [
    path('contact/', contact_view, name='contact'),
    path('student_add/', ProcessStudent.as_view(), name='student_add'),
    path('', MainPage.as_view(), name='main'),
]
