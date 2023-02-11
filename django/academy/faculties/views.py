from django.views.generic import ListView

from faculties.models import Faculty


class MainPage(ListView):
    model = Faculty
    template_name = 'faculties/index.html'

