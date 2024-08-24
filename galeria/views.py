from django.shortcuts import render
from galeria.models import Fotografia





def index(request):
    
    fotografias = Fotografia.objects.all()

    
    
    return render(request, 'tp_galeria/index.html', {"cards": fotografias})


def view_imagem(request):
    return render(request, 'tp_galeria/imagem.html')

# Create your views here.
