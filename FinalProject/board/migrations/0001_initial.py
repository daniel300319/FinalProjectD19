# Generated by Django 5.0.1 on 2024-01-30 17:03

import ckeditor_uploader.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Заголовок')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Текст')),
                ('category', models.CharField(choices=[('tanks', 'Танки'), ('healers', 'Хилы'), ('damage_dealers', 'ДД'), ('merchants', 'Торговцы'), ('guild_masters', 'Гилдмастеры'), ('quest_givers', 'Квестгиверы'), ('blacksmiths', 'Кузнецы'), ('tanners', 'Кожевники'), ('potion_makers', 'Зельевары'), ('spell_masters', 'Мастера заклинаний')], max_length=15, verbose_name='Категория')),
                ('date_of_creation', models.DateField(auto_now_add=True)),
                ('time_of_creation', models.TimeField(auto_now_add=True)),
                ('datetime_of_creation', models.DateTimeField(auto_now_add=True)),
                ('date_of_last_update', models.DateField(auto_now=True)),
                ('time_of_last_update', models.TimeField(auto_now=True)),
                ('datetime_of_last_update', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Манчкин')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=1500)),
                ('confirmed', models.BooleanField(blank=True, null=True, verbose_name='Подтвержден')),
                ('date_of_creation', models.DateField(auto_now_add=True)),
                ('time_of_creation', models.TimeField(auto_now_add=True)),
                ('datetime_of_creation', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.post')),
            ],
        ),
    ]
