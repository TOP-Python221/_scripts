from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from faculties.models import Faculty, Department, Group
from faculties.forms import GroupAdd


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


def department_view(request, pk: int):
    dep = Department.objects.get(pk=pk)
    if request.method == 'GET':
        return render(
            request,
            'faculties/department.html',
            {
                'page_title': dep.acronym.upper(),
                'object': dep,
                'form': GroupAdd(),
            }
        )
    elif request.method == 'POST':
        form = GroupAdd(request.POST)
        if form.is_valid():
            Group(
                **form.cleaned_data,
                department_id=pk,
            ).save()
        return redirect(f'{dep.faculty.acronym}_{dep.acronym}', pk=pk)


def contact_view(request):
    return HttpResponse()
