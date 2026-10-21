from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from .models import *


_INPUT_CLASS = (
    'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg '
    'focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 ps-4 '
    'dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 '
    'dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
)


class SuporteModelForm(forms.ModelForm):
    class Meta:
        model = Suporte
        fields = ['nome', 'email', 'assunto', 'mensagem']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': _INPUT_CLASS,
                'placeholder': 'Seu nome',
            }),
            'email': forms.EmailInput(attrs={
                'class': _INPUT_CLASS,
                'placeholder': 'Seu email',
            }),
            'assunto': forms.Select(attrs={'class': _INPUT_CLASS}),
            'mensagem': forms.Textarea(attrs={
                'class': _INPUT_CLASS,
                'placeholder': 'Digite sua mensagem',
                'rows': 4,
            }),
        }


class FiltroTopico(forms.Form):
    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.all(),
        required=False,
        empty_label='Selecione uma categoria',
        widget=forms.Select(attrs={'class': _INPUT_CLASS + ' cursor-pointer'}),
    )

    nivel_experiencia = forms.ChoiceField(
        choices=[
            ('', 'Selecione um nível de experiência'),
            ('Iniciante', 'Iniciante'),
            ('Intermediário', 'Intermediário'),
            ('Avançado', 'Avançado'),
        ],
        required=False,
        widget=forms.Select(attrs={'class': _INPUT_CLASS + ' cursor-pointer'}),
    )

    funcao = forms.ModelChoiceField(
        queryset=AreaAtuacao.objects.all(),
        required=False,
        empty_label='Selecione uma função',
        widget=forms.Select(attrs={'class': _INPUT_CLASS + ' cursor-pointer'}),
    )

    ordenar_por = forms.ChoiceField(
        choices=[
            ('', 'Ordenar por'),
            ('-created_at', 'Mais recentes'),
            ('created_at', 'Mais antigos'),
        ],
        required=False,
        widget=forms.Select(attrs={'class': _INPUT_CLASS + ' cursor-pointer'}),
    )


class RegistroForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': _INPUT_CLASS, 'placeholder': 'E-mail'}),
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': _INPUT_CLASS,
            'placeholder': 'Nome de usuário',
        })
        self.fields['password1'].widget.attrs.update({
            'class': _INPUT_CLASS,
            'placeholder': 'Senha',
        })
        self.fields['password2'].widget.attrs.update({
            'class': _INPUT_CLASS,
            'placeholder': 'Confirme a senha',
        })


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': _INPUT_CLASS,
            'placeholder': 'Nome de usuário',
        })
        self.fields['password'].widget.attrs.update({
            'class': _INPUT_CLASS,
            'placeholder': 'Senha',
        })
