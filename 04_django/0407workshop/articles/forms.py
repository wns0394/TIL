from django import forms
from .models import Article

# class ArticleForm(forms.Form):
    # title = forms.CharField(max_length=10)
    # content = forms.CharField(widget=forms.Textarea)

    
class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs = {
                'class' : 'my-title',
                'placeholder': '제목을 입력하시오'
            }
        )
    )
    content = forms.CharField(
        widget=forms.TextInput(
            attrs = {
                'class': 'my-content',
                'placeholder': '내용을 입력하시오'
            }
        )
    )
    class Meta:
        model = Article
        fields = '__all__'
