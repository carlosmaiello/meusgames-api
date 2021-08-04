from rest_framework import serializers
from meusgames.games.models import Categoria, Game

class CategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categoria
        fields = '__all__'

class GameSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer(read_only=True)
    
    class Meta:
        model = Game
        fields = '__all__'