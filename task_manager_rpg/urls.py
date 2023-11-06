
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from tasks.api.viewsets import TasksViewSet

router = routers.DefaultRouter()
router.register(r'tasks',TasksViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include(router.urls)),
]
