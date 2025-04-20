from django import forms
from .models import Socio

class SocioForm(forms.ModelForm):
    class Meta:
        model = Socio
        fields = '__all__'  
        widgets = {
            'rut': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese su RUT',
                'onblur': 'validarRut()',
            }),
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese su Nombre',
            }),
            'apellidop': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese su Apellido Paterno',
            }),
            'apellidom': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese su Apellido Materno',
            }),
            'direccion': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese su dirección',
            }),
            'comuna': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese su comuna',
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese su número',
                'onblur': 'validarTelefono()',
            }),
            'correo': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese su correo',
            }),
            'region': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese su región',
            }),
            'contrasena': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese contraseña',
                'onblur': 'validarContrasena()',
            }),
        }
