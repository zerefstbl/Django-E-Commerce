from distutils.command.clean import clean
from django import forms
from . import models
from django.contrib.auth.models import User
from pprint import pprint


class PerfilForm(forms.ModelForm):
    class Meta:
        model = models.Perfil
        fields = '__all__'
        exclude = ('usuario',)


class UserForm(forms.ModelForm):
    password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(),
        label='Senha'
    )

    password2 = forms.CharField(
        required=False,
        widget=forms.PasswordInput(),
        label='Confirmação de Senha'
    )

    def __init__(self, usuario=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.usuario = usuario

    class Meta:
        model = User
        fields = ('username', 'last_name', 'first_name',
                  'password', 'password2', 'email')

    def clean(self, *args, **kwargs):
        data = self.data
        cleaned = self.cleaned_data
        validation_error_msgs = {}

        usuario_data = cleaned.get('username')
        password_data = cleaned.get('password')
        password2_data = cleaned.get('password2')
        email_data = cleaned.get('email')

        pprint(usuario_data)

        usuario_db = User.objects.filter(username=usuario_data).first()

        if self.usuario:
            validation_error_msgs['username'] = 'blablabla'
            print('sdoods')
        else:
            print('dfisiufdh')

        if validation_error_msgs:
            raise(forms.ValidationError(validation_error_msgs))
