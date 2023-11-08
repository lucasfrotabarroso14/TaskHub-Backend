from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from account.api.serializers import AccountSerializer, LoginSerializer


class AccountViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [permissions.AllowAny]

    @action(detail =  False, methods = ['post'])
    def register(self,request,*args,**kwargs):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            res = {
                "refresh" : str(refresh),
                "access": str(refresh.access_token)
            }
            return Response(res, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    @action(detail = False, methods=['post'])
    def login(self, request, *args, **kwargs):
        serializer = LoginSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            refresh = RefreshToken.for_user(user)
            res = {
                "refresh":str(refresh),
                "access": str(refresh.access_token)
            }
            return Response(res,status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

