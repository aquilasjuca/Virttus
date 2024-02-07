from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('contatos/', views.contatos, name='contatos'),
    path('profissionais/', views.profissionais, name='profissionais'),
    path('serviços/', views.servicos, name='servicos'),
    path('localização/', views.localizacao, name='localizacao')
]
