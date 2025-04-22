from django import forms
from .models import Socio
import re

class SocioForm(forms.ModelForm):
    class Meta:
        model = Socio
        fields = '__all__'
        widgets = {
            'rut': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Formato de RUT: 12345678-9',
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
                'placeholder': 'El número debe tener 9 dígitos',
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

        labels = {
            'rut': 'RUT',
            'nombre': 'Nombre',
            'apellidop': 'Apellido Paterno',
            'apellidom': 'Apellido Materno',
            'direccion': 'Dirección',
            'comuna': 'Comuna',
            'telefono': 'Teléfono',
            'correo': 'Correo Electrónico',
            'region': 'Región',
            'contrasena': 'Contraseña',
        }

    # Validación de RUT chileno simple (sin puntos, con guion)
    def clean_rut(self):
        rut = self.cleaned_data['rut']
        if not re.match(r'^\d{7,8}-[\dkK]$', rut):
            raise forms.ValidationError('Formato de RUT inválido. Ej: 12345678-9')
        return rut

    # Validación de teléfono chileno
    def clean_telefono(self):
        telefono = self.cleaned_data['telefono']
        if not re.match(r'^9\d{8}$', telefono):
            raise forms.ValidationError('El número debe tener 9 dígitos y comenzar con 9')
        return telefono

    # Validación de correo (ya la hace el campo EmailField, pero la reforzamos)
    def clean_correo(self):
        correo = self.cleaned_data['correo']
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', correo):
            raise forms.ValidationError('Correo electrónico no válido')
        return correo

    # Validación de contraseña segura
    def clean_contrasena(self):
        contrasena = self.cleaned_data['contrasena']
        if len(contrasena) < 6:
            raise forms.ValidationError('La contraseña debe tener al menos 6 caracteres')
        if not re.search(r'[A-Za-z]', contrasena):
            raise forms.ValidationError('Debe contener al menos una letra')
        if not re.search(r'\d', contrasena):
            raise forms.ValidationError('Debe contener al menos un número')
        if not re.search(r'[@$!%*#?&]', contrasena):
            raise forms.ValidationError('Debe contener al menos un carácter especial (@, $, !, %, *, etc)')
        return contrasena
