# Generated by Django 3.2.6 on 2021-08-04 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='dataLancamento',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='dataUltimoJogo',
            field=models.DateTimeField(blank=True),
        ),
    ]
