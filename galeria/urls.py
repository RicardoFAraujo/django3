from django.urls import path
from galeria.views import index, view_imagem

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>', view_imagem, name='imagem'),
]