from rest_framework.serializers import ModelSerializer

from tasks.models import Task


class TasksSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ['id_task','titulo','descricao','data_conclusao']