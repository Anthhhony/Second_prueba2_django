from django import forms
from finalApp2.models import DBproyecto

class formulario(forms.Form):
    rut = forms.CharField(max_length=12)
    nombre = forms.CharField(max_length=30)
    telefono = forms.IntegerField()
    edad = forms.IntegerField()
    correo = forms.EmailField()

class FormularioChetado(forms.ModelForm):
    class Meta:
        model = DBproyecto
        fields = "__all__"