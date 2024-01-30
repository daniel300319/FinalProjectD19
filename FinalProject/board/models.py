from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

CATEGORIES = (
        ('tanks', 'Танки'),
        ('healers', 'Хилы'),
        ('damage_dealers', 'ДД'),
        ('merchants', 'Торговцы'),
        ('guild_masters', 'Гилдмастеры'),
        ('quest_givers', 'Квестгиверы'),
        ('blacksmiths', 'Кузнецы'),
        ('tanners', 'Кожевники'),
        ('potion_makers', 'Зельевары'),
        ('spell_masters', 'Мастера заклинаний'),
    )

class Post(models.Model):
    title = models.CharField('Заголовок', max_length=256)
    text = RichTextUploadingField('Текст')
    category = models.CharField(max_length=15, choices=CATEGORIES, verbose_name='Категория')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Манчкин')

    date_of_creation = models.DateField(auto_now_add=True)
    time_of_creation = models.TimeField(auto_now_add=True)
    datetime_of_creation = models.DateTimeField(auto_now_add=True)

    date_of_last_update = models.DateField(auto_now=True)
    time_of_last_update = models.TimeField(auto_now=True)
    datetime_of_last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.category} {self.title}'


class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.name}'


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=1500)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    confirmed = models.BooleanField('Подтвержден', null=True, blank=True)

    date_of_creation = models.DateField(auto_now_add=True)
    time_of_creation = models.TimeField(auto_now_add=True)
    datetime_of_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author} {self.date_of_creation} {self.time_of_creation.__format__("%H:%M:%S")}'