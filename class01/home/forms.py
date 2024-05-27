from django import forms
from .models import *

class SuporteModelForm(forms.ModelForm):
    class Meta:
        model = Suporte
        fields = '__all__'