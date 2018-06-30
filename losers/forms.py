from django import forms

class FormContacto(forms.Form):

    nombre = forms.CharField(required=True,max_length=200,widget=forms.TextInput(attrs={'placeholder':'Nombre','autocomplete':'off'}))
    correo = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'Correo','autocomplete':'off'} ))
    mensaje = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Mensaje','autocomplete':'off'}),max_length=None)