from meusgames.games.api.serializers import CategoriaSerializer, GameSerializer
from rest_framework import mixins
from rest_framework import viewsets, status

from meusgames.games.models import Categoria, Game

class CategoriaViewSet(mixins.ListModelMixin,                     
                     mixins.RetrieveModelMixin,                     
                     viewsets.GenericViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer    



class GameViewSet(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    #permission_classes = (IsAuthenticated,)
    queryset = Game.objects.all()
    serializer_class = GameSerializer
