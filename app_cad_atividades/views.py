from django.shortcuts import render
from .models import Atividade
def home(request):
    return render(request, 'atividades/home.html')


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

    return render(request, 'atividades/atividades.html', atividades)