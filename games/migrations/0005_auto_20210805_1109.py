# Generated by Django 3.2.6 on 2021-08-05 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0004_alter_game_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='dataLancamento',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='dataUltimoJogo',
            field=models.DateTimeField(null=True),
        ),
    ]
