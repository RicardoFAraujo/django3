from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografia





def index(request):
    
    fotografias = Fotografia.objects.all()

    
    
    return render(request, 'tp_galeria/index.html', {"cards": fotografias})


def view_imagem(request, foto_id):
    fotografia= get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'tp_galeria/imagem.html', {"fotografia": fotografia})

# Create your views here.
