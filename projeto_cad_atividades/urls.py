from django.contrib import admin
from django.urls import path
from app_cad_atividades import views

urlpatterns = [
    #rota, view responsavel, nome referencia
    path('', views.home,name='home'),
    path('atividades/',views.atividades,name='listagem_atividades'),
    #path('admin/', admin.site.urls),
]
