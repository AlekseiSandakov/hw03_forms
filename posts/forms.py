from django.forms import ModelForm

from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['text', 'group']
        labels = {
            'text': 'Текст записи',
            'group': 'Группа'
        }
        help_texts = {
            'text': 'Введите текст новой записи',
            'group': 'Укажите группу'
        }
