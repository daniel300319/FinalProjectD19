from django import forms
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Post, Comment, CATEGORIES


class PostCreateForm(forms.ModelForm):

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