from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

from .models import *


class PostCreateForm(forms.ModelForm):
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

    title = forms.CharField(label='Заголовок', widget=forms.TextInput(attrs={'class': 'form-control'}))
    text = forms.CharField(label='Текст', widget=CKEditorUploadingWidget(attrs={'class': 'form-control'}))
    category = forms.ChoiceField(
        label='Категория',
        widget=forms.Select(attrs={'class': 'form-select'}),
        choices=CATEGORIES
    )

    class Meta:
        model = Post
        exclude = ('author',)


class CommentCreateForm(forms.ModelForm):
    text = forms.CharField(label='Текст', widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Comment
        fields = ('text',)