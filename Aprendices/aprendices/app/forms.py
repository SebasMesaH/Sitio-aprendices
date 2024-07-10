from django import forms
from .import models

class Aprendizform(forms.ModelForm):
    class meta:
        models = models.Aprendiz
        fields = '__all__'