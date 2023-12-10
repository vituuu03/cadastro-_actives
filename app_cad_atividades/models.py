from django.db import models

# Create your models here.
class Atividade(models.Model):
    id_atividades = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    data = models.DateField(auto_now=True)
    atividades = models.TextField(max_length=255)
    STATUS_CHOICES = (
        ('pendente', 'Pendente'),
        ('concluido', 'Concluído'),
        ('cancelado', 'Cancelado'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')