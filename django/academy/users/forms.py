from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User
from django.forms import EmailField


class UserRegisterForm(UserCreationForm):
    email = EmailField(
        help_text='Enter your valid e-mail address.',
        error_messages={
            'invalid': 'Enter the correct e-mail address.',
        }
    )
    email.widget.attrs.update({
        'class': 'form-control',
    })

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']
        field_classes = {"username": UsernameField}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'input_username',
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'input_password1',
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'input_password2',
        })
