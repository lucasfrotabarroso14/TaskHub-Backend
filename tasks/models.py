from django.contrib.auth.models import User
from django.db import models

class Task(models.Model):
    id_task = models.AutoField(primary_key =True)
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    data_criacao = models.DateField(auto_now_add=True, null=True)
    data_conclusao = models.DateField(null = True, blank=True)
    DIFICULDADE_CHOICES = [
        ('Facil','Facil'),
        ('Medio','Medio'),
        ('Dificil','Dificil')
    ]
    dificuldade = models.CharField(max_length=20,choices=DIFICULDADE_CHOICES)
    id_user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    STATUS_CHOICES = [
        ('Pendente', 'Pendente'),
        ('Em Andamento', 'Em Andamento'),
        ('Concluido', 'Concluido')
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, null=True)
    def __str__(self):
        return self.titulo
