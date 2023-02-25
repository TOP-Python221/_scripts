from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.views.generic import FormView

from users.forms import UserRegisterForm


class RegisterView(FormView):
    form_class = UserRegisterForm
    template_name = 'registration/register.html'
    success_url = '/authorize/login/'

    def form_valid(self, form):
        form.save()
        return redirect(self.success_url)

