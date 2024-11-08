# Generated by Django 5.1.3 on 2024-11-08 00:08

import django.db.models.deletion
import pathlib
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('curso', models.CharField(max_length=50)),
                ('sinopse', models.TextField(blank=True, max_length=150)),
                ('instagram', models.URLField(blank=True)),
                ('linkedin', models.URLField(blank=True)),
                ('github', models.URLField(blank=True)),
                ('website', models.URLField(blank=True)),
                ('profile_picture', models.ImageField(upload_to=pathlib.PurePosixPath('/app/profile_pictures'))),
                ('descricao_longa', models.TextField(blank=True)),
                ('network', models.ManyToManyField(blank=True, to='app.userprofile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Perfil',
                'verbose_name_plural': 'Perfis',
                'ordering': ['curso', 'first_name'],
            },
        ),
    ]
