from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from faculties.models import Faculty


class MainPage(ListView):
    model = Faculty
    template_name = 'faculties/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view'] = 'main'
        return context


class FacultiesExtended(DetailView):
    model = Faculty
    template_name = 'faculties/faculty_extended.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context |= {
            'object_list': self.get_queryset(),
            'view': 'faculty',
            'id': self.object.id,
        }
        return context


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
