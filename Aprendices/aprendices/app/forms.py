from django import forms
from .models import Aprendiz

class Aprendizform(forms.ModelForm):
    class Meta:
        model = Aprendiz
        fields = '__all__'