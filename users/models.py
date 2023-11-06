from django.db import models

class UserModel(models.Model):
    id_user = models.AutoField(primary_key = True)
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)
    FUNCAO_CHOICES = [
        ('Aministrador','Administrador'),
        ('Tech Lead', 'Tech Lead'),
        ('Desenvolvedor', 'Desenvolvedor')
    ]
    funcao = models.CharField(max_length=20, choices=FUNCAO_CHOICES)