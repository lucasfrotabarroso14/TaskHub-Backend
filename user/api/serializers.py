from rest_framework.serializers import ModelSerializer

from user.models import UserProfile


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user','funcao','id_equipe']