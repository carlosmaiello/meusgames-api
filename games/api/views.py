from .serializers import  CategoriaSerializer,GameSerializer, UserSerializer
from rest_framework import generics, mixins, viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


from games.models import Categoria, Game
from django.contrib.auth.models import User
from .serializers import RegisterSerializer


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserMeView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(id=self.request.user.id).get()
        serializer = self.get_serializer(queryset)
        return Response(serializer.data)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer



class CategoriaViewSet(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
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

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)
