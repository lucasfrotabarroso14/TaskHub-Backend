
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from tasks.api.viewsets import TaskViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# from users.api.viewsets import CustomUserViewSet
from users.api.viewsets import UserViewSet

router = routers.DefaultRouter()
router.register(r'tasks',TaskViewSet)
router.register(r'users',UserViewSet, basename='user')

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('api/token/refresh.', TokenRefreshView.as_view(),name='token_refresh'),
    path("admin/", admin.site.urls),
    path('', include(router.urls)),
]
