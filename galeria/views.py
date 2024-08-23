from django.shortcuts import render

def index(request):
    return render(request, 'tp_galeria/index.html')

# Create your views here.
