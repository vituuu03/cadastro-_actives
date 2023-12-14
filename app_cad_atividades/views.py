#imports necessários
from django.shortcuts import render
from .models import Atividade

#criando a função home
#serve para renderizar a página home.html
def home(request):
    return render(request, 'atividades/home.html')

#criando a função atividades
#serve para renderizar a página atividades.html
def atividades(request):
    nova_atividade = Atividade()
    nova_atividade.nome = request.POST.get('nome')
    nova_atividade.data = request.POST.get('data')
    nova_atividade.atividades = request.POST.get('atividades')
    nova_atividade.status = request.POST.get('status')
    nova_atividade.save()

    atividades={
            'atividades': Atividade.objects.all()
    }

    return render(request, 'atividades/listagem.html', atividades)

#criando a função para visualizar a página index.html
#serve para renderizar a página index.html
def homePageView(request):
    return render(request, 'homepage/index.html')


#criando a função para visualizar a página listagem.html
#serve para renderizar a lista de atividades
def mostrarListaAtividades(request):
    atividades={
            'atividades': Atividade.objects.all()
    }

    return render(request, 'atividades/listagem.html', atividades)

