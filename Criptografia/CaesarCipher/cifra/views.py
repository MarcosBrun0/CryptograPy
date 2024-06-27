from django.shortcuts import render
from .forms import CifraForm

def home_view(request):
    return render(request, 'cifra/home.html')


def cifra_de_cesar(texto, deslocamento):
    resultado = ""
    for char in texto:
        if char.isalpha():
            deslocamento_base = ord('A') if char.isupper() else ord('a')
            char_code = ord(char)
            novo_char_code = (char_code - deslocamento_base + deslocamento) % 26 + deslocamento_base
            resultado += chr(novo_char_code)
        else:
            resultado += char
    return resultado

def cifra_view(request):
    if request.method == 'POST':
        form = CifraForm(request.POST)
        if form.is_valid():
            texto = form.cleaned_data['texto']
            deslocamento = form.cleaned_data['deslocamento']
            resultado = cifra_de_cesar(texto, deslocamento)
            return render(request, 'cifra/resultado.html', {'resultado': resultado})
    else:
        form = CifraForm()
    return render(request, 'cifra/index.html', {'form': form})
