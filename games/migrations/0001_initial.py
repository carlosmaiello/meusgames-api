# Generated by Django 3.2.6 on 2021-08-04 14:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('dataLancamento', models.DateTimeField()),
                ('preco', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('horasJogadas', models.IntegerField(default=0)),
                ('concluido', models.BooleanField(default=False)),
                ('dataUltimoJogo', models.DateTimeField()),
                ('avaliacao', models.IntegerField(default=0)),
                ('comentario', models.TextField(blank=True, default='')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='games.categoria')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
