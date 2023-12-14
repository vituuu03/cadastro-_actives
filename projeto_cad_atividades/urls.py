#imports necessários
from django.contrib import admin
from django.urls import path
from app_cad_atividades import views

#criando as rotas
urlpatterns = [
    #url para visualizar a table de atividades
    path('tableAtividades/',views.mostrarListaAtividades,name='table_atividades'),
    #url para visualizar a pagina de login do superuser e cadastrar novas atividades
    path('admin/', admin.site.urls),
    #url renderiza a pagina principal do projeto
    path('', views.homePageView, name='index')
]
