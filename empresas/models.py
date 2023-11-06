from django.db import models

class Empresa(models.Model):
    id_empresa = models.AutoField(primary_key = True)
    nome_empresa = models.CharField(max_length=150)
    # id_administrador foreign key