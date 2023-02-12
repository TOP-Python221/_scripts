from django.http import HttpResponse
from django.views.generic import ListView, DetailView, FormView

from faculties.models import Faculty


class MainPage(ListView):
    model = Faculty
    template_name = 'faculties/index.html'


class FacultyView(DetailView):
    model = Faculty
    template_name = 'faculties/faculty.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        students = sum(
            1
            for dep in self.object.department_set.all()
            for gr in dep.group_set.all()
            for _ in gr.students.all()
        )
        context['students'] = students
        return context


def contact_view(request):
    return HttpResponse()
