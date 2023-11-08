from rest_framework.serializers import ModelSerializer

from tasks.models import Task


class TasksSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ['id_task','titulo','descricao','dificuldade','data_criacao','data_conclusao','id_user']