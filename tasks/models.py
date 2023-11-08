from django.contrib.auth.models import User
from django.db import models

class Task(models.Model):
    id_task = models.AutoField(primary_key =True)
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    data_criacao = models.DateField(auto_now_add=True)
    data_conclusao = models.DateField(null = True, blank=True)
    DIFICULDADE_CHOICES = [
        ('Facil','Fácil'),
        ('Medio','Medio'),
        ('Dificil','Dificil')
    ]
    dificuldade = models.CharField(max_length=20,choices=DIFICULDADE_CHOICES)
    id_user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.titulo
