from rest_framework.serializers import ModelSerializer

from tasks.models import Tasks


class TasksSerializer(ModelSerializer):
    class Meta:
        model = Tasks
        fields = ['id_task','titulo','descricao','data_conclusao']