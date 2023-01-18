from django import forms

class EspecialidadesFormulario(forms.Form):
    
    especialidad = forms.CharField()
    adulto = forms.BooleanField()
    pediatrico = forms.BooleanField()

class StaffFormulario(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    profesion = forms.CharField()

