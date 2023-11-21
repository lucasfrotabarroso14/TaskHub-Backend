
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from equipes.api.viewsets import EquipeViewSet
from tasks.api.viewsets import TaskViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# from account.api.viewsets import CustomUserViewSet
from account.api.viewsets import AccountViewSet
from user.api.viewsets import UserProfileViewSet

router = routers.DefaultRouter()
router.register(r'tasks',TaskViewSet)

router.register(r'account',AccountViewSet, basename='account')
router.register(r'teams',EquipeViewSet)
router.register('user/profile',UserProfileViewSet)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('api/token/refresh.', TokenRefreshView.as_view(),name='token_refresh'),
    path("admin/", admin.site.urls),
    path('', include(router.urls)),
]
