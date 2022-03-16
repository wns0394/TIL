import re
from django.shortcuts import render
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    # <QuerySet [<Article;django>,<Article;django>,...]
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    # print(title, content)
    # 게시글 생성
    #
    ''' 
    첫 번째 방법
    article = Article()
    article.title = title
    article.content = content
    article.save()
    '''

    # 
    '''
    두번째 방법
    article = Article(title=title, content=content)
    article.save()
    '''

    # 세번째 방법
    Article.objects.create(title=title, content=content)

    # article 정보를 담아서 넘겨주자...
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)