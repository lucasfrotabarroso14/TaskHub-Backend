from django.db import models

# from users.models import Users


class Equipe(models.Model):
    id_equipe = models.AutoField(primary_key = True)
    nome_equipe = models.CharField(max_length=100)
    # lider = models.ForeignKey(Users,on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_equipe