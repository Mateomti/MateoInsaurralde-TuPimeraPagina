from django import forms


class RegistroProducto(forms.Form):
    codigo = forms.IntegerField()
    nombre = forms.CharField(max_length=20)
    cantidad = forms.IntegerField()