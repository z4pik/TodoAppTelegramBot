from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import ToDoListUser
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = ToDoListUser
        fields = ['username', 'email', 'password1', 'password2']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = ToDoListUser
        fields = ['username', 'email', 'telegram_id']

    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Сохранить'))
