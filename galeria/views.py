from django.shortcuts import render

def index(request):
    return render(request, 'tp_galeria/index.html')


def view_imagem(request):
    return render(request, 'tp_galeria/imagem.html')

# Create your views here.
