from django.forms import ModelForm, widgets, TextInput, EmailInput
from.models import DataBase

class Form(ModelForm):
    class Meta:
        fields = '__all__'
        model = DataBase
        widgets = {
             'first': TextInput(attrs={
                'class': "form",
                'placeholder': "Name"
                }),
        }