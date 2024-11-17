# Generated by Django 5.1.3 on 2024-11-17 14:36

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id_eventos', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
                ('data', models.DateField()),
                ('local', models.CharField(max_length=255)),
                ('Ano_lancamento', models.IntegerField()),
                ('DiaAdi', models.DateField(auto_now_add=True)),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Participante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=35)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participantes', to='api.evento')),
            ],
        ),
    ]
