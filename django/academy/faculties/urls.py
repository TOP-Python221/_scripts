from django.urls import path

from faculties.models import Faculty
from faculties.views import MainPage, FacultyView, FacultiesExtended, contact_view

urlpatterns = []

for faculty in Faculty.objects.all():
    urlpatterns += [path(
        f'{faculty.acronym}/',
        # FacultyView.as_view(),
        FacultiesExtended.as_view(),
        kwargs={'pk': faculty.id},
        name=f'{faculty.acronym}',
    )]

urlpatterns += [
    path('contact/', contact_view, name='contact'),
    path('', MainPage.as_view(), name='main'),
]
