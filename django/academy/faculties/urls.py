from django.urls import path

from faculties.views import MainPage

urlpatterns = [
    path('', MainPage.as_view(), name='main')
]
