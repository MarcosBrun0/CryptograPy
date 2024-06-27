from django import forms

class CifraForm(forms.Form):
    texto = forms.CharField(widget=forms.Textarea, label='Texto')
    deslocamento = forms.IntegerField(label='Deslocamento')
