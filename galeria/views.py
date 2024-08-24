from django.shortcuts import render





def index(request):
    dados = {
    1: {"nome":"Nebulosa de Carina",
        "legenda":"webbtelescope.org / NASA / James Webb"},
    2: {"nome":"Galáxia NGC 1079",
        "legenda":"nasa.org / NASA / Hubble"}
    }
    
    
    return render(request, 'tp_galeria/index.html', {"cards": dados})


def view_imagem(request):
    return render(request, 'tp_galeria/imagem.html')

# Create your views here.
