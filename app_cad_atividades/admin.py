#import necessário para registrar o modelo Atividade no painel de administração
from django.contrib import admin

#importando o modelo Atividade
from .models import Atividade

#registrando o modelo Atividade no painel de administração
admin.site.register(Atividade)
