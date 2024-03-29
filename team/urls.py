from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import TeamViewSet, UserDetail, get_my_team, add_member

router = DefaultRouter()
router.register('teams', TeamViewSet, basename='teams')

urlpatterns = [
    path('teams/member/<int:pk>/', UserDetail.as_view(), name='userdetail'),
    path('teams/get_my_team/', get_my_team, name='get_my_team'),
    path('teams/add_member/', add_member, name='add_member'),
    path('', include(router.urls)),
]


