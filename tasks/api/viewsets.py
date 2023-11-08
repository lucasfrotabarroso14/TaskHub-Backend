from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from tasks.api.serializers import TasksSerializer
from tasks.models import Task

from utils.responses import DefaultResponse


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TasksSerializer

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.filter_queryset(self.get_queryset())
            serializer = self.get_serializer(queryset, many=True)
            response = DefaultResponse(status_code=200,status=True,message="Busca realizada com sucesso", result = serializer.data)
            return Response(response.to_json())
        except Exception as e:
            response = DefaultResponse(status_code=500,status=False, message="Erro na busca dos dados", result = e)
            return Response(response.to_json())


    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                response = DefaultResponse(status_code=201, status= True, message = 'Task criada com sucesso',
                                           result=serializer.data)
                return Response(response.to_json())
            else:
                response = DefaultResponse(status_code=400, status= False, message = 'Dados inválidos',
                                           result=serializer.errors)
                return Response(response.to_json())
        except Exception as e:
            response = DefaultResponse(status_code=500, status=False, message='Erro na criação da task',
                                       result=str(e))
            return Response(response.to_json(), status=500)

    def update(self, request, *args, **kwargs):
        try:
            data = self.get_object()
            serializer = self.get_serializer(data, data = request.data)
            if serializer.is_valid():
                serializer.save()
                response = DefaultResponse(status_code=201, status=True, message='Task atualizada com suceso',
                                           result=serializer.data)
                return Response(response.to_json())
            else:
                response = DefaultResponse(status_code=400, status=False, message='Dados inválidos',
                                           result=serializer.errors)
                return Response(response.to_json())

        except Exception as e:
            response = DefaultResponse(status_code=500, status=False, message='Erro na atualização do objeto',
                                       result=str(e))
            return Response(response.to_json(), status=500)

    def destroy(self, request, *args, **kwargs):
        try:
            data = self.get_object()
            data.delete()
            response = DefaultResponse(status_code=201, status=True, message='Task excluida com suceso',
                                   result=None)
            return Response(response.to_json())

        except Exception as e:
            response = DefaultResponse(status_code=500, status=False, message="Erro na exclusão do objeto",
                                       result=str(e))
            return Response(response.to_json(), status=500)






