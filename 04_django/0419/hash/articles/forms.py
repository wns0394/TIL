from django import forms
from .models import Article, Comment


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        exclude = ('user', 'like_users', 'hashtags',)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('content',)
