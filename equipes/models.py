from django.contrib.auth.models import User
from django.db import models


class Equipe(models.Model):
    id_equipe = models.AutoField(primary_key = True)
    nome_equipe = models.CharField(max_length=100)
    lider = models.OneToOneField(User,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nome_equipe

    #tem que ver quais os users
