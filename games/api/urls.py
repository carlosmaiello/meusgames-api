from django.urls import path
from rest_framework.routers import DefaultRouter

from ..api.views import CategoriaViewSet, GameViewSet

app_name = 'games'

router = DefaultRouter()
router.register('categorias', CategoriaViewSet)
router.register('games', GameViewSet)
