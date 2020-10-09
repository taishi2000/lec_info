from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = {'title', 'text'}
        widgets = {
              'title': forms.TextInput(attrs={
              'class': 'form-control'
            }),
              'text': forms.TextInput(attrs={
              'class': 'form-control'
            }),
        }
        labels = {
            'title': 'タイトル',
            'text': '本文',
        }

    def clean(self):
        data = super().clean()
        title = data.get('title')
        text = data.get('text')
        if len(title) > 10:
            msg = "タイトルは10文字以内にしてください"
            self.add_error('title', msg)
        if len(text) > 15:
            msg = "本文は15文字以内にしてください"
            self.add_error('text', msg)
