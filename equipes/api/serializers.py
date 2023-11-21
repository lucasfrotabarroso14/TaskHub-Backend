from rest_framework.serializers import ModelSerializer
from equipes.models import Equipe


class EquipeSerializer(ModelSerializer):
    class Meta:
        model = Equipe
        fields = ['id_equipe','nome_equipe','lider']