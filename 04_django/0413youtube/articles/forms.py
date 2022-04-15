
from django import forms
from .models import Article, Comment


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        # fields = '__all__'
        exclude = ('user',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        # fields = '__all__' 이거 하면 댓글 쓰는게 Article 칸이랑 Content칸이랑 2개 나온다. 우리는 Content만 원한다.
        fields = ('content',)