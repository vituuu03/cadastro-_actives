from django.db import models

#criando a classe Atividade
#serve para criar a tabela no banco de dados
class Atividade(models.Model):
    id_atividades = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    data = models.DateField()
    atividades = models.TextField(max_length=255)
    STATUS_CHOICES = (
        ('pendente', 'Pendente'),
        ('concluido', 'Concluído'),
        ('cancelado', 'Cancelado'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')

