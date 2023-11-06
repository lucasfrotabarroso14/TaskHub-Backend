from django.db import models

class Tasks(models.Model):
    id_task = models.AutoField(primary_key = True)
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    data_conclusao = models.DateField()

    def __str__(self):
        return self.titulo
