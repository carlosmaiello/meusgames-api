from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False)

# Create your models here.
class Game(models.Model):
    categoria = models.ForeignKey(Categoria, null=False, on_delete=models.RESTRICT)
    usuario = models.ForeignKey(User, null=False, on_delete=models.RESTRICT)
    nome = models.CharField(max_length=255, blank=False, null=False)
    dataLancamento = models.DateTimeField()
    preco = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    horasJogadas= models.IntegerField(null=False, default=0)
    concluido = models.BooleanField(null=False, default=False)
    dataUltimoJogo = models.DateTimeField()
    avaliacao = models.IntegerField(null=False, default=0)
    comentario = models.TextField(default="", blank=True)
