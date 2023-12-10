#imports necessários
from django.contrib import admin
from django.urls import path
from app_cad_atividades import views

#criando as rotas
urlpatterns = [
    
    #rota para a página home
    #o caminho é vazio, pois é a página inicial, url padrão,ou seja, localhost:8000
    path('', views.home,name='home'),
    #rota para a página atividades
    #o caminho é atividades, pois é a página que será renderizada, url padrão,ou seja, localhost:8000/atividades
    #porem se colocado na url, nao funcionará, pois é necessário um cadastro de atividades antes
    path('atividades/',views.atividades,name='listagem_atividades'),
    #path('admin/', admin.site.urls), (rota padrão do django), porem não necessaria para o pj
]
