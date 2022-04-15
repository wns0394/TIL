from ssl import ALERT_DESCRIPTION_CLOSE_NOTIFY
from django import forms
from . models import Article

# class ArticleForm(forms.Form):
    # title = forms.CharField(max_length=100)
    # content = forms.CharField(widget=forms.Textarea)

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = '__all__'