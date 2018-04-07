from django import forms

class FormContacto(forms.Form):

    nombre = forms.CharField(required=True,max_length=200,widget=forms.TextInput(attrs={'placeholder':'Nombre'}))
    correo = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'Correo'}))
    mensaje = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Mensaje'}),max_length=None)