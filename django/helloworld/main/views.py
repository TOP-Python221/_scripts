from django.http import HttpResponse


def main_view(request):
    return HttpResponse('Hello World!')

