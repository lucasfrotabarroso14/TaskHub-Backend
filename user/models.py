from django.db import models
from django.db import models
from django.contrib.auth.models import User


from equipes.models import Equipe


class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    id_equipe = models.ForeignKey(Equipe,on_delete=models.SET_NULL,null = True,related_name='membros')
    FUNCOES_CHOICES = [
        ('Tech-Lead','Tech Lead'),
        ('Dev-Front-End','Dev Front-End'),
        ('Dev-Back-End', 'Dev Back-End'),
        ('Dev-Full-Stack','Dev Full-Stack')
    ]
    funcao = models.CharField(max_length=100,choices=FUNCOES_CHOICES, null = True)

    def __str__(self):
        return self.user.username
