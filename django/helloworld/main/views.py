from django.http import HttpResponse
from django.shortcuts import render


def main_view(request):
    return HttpResponse('<h1>First Django Project</h1>\n'
                        '<p>Hello World!</p>')


def about_view(request):
    return render(request, 'main/about.html')

