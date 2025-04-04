from django import forms
from django.utils import timezone
from .models import Consulta

class Formulario_consulta(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['paciente', 'data', 'medico', 'status']
        widgets = {
            'data': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }
        labels = {
            'data': 'Data e Hora (futuro)'
        }

    def clean_data(self):
        data = self.cleaned_data['data']
        if data < timezone.now():
            raise forms.ValidationError("A data deve ser futura!")
        return data