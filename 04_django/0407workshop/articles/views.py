from django.shortcuts import render,redirect
from .models import Article
from .forms import ArticleForm
 
# Create your views here.

def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }

    return render(request, 'articles/index.html',context)

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')

    else:
        form = ArticleForm()
    context = {
        'form' : form
    }
    return render(request, 'articles/create.html', context)

def detail(request, article_pk):
    # 이걸 변수로 저장해주어야한다.
    # Article.objects.get(pk=article_pk)
    article = Article.objects.get(pk=article_pk)
    context = {
        'article' : article
    }

    return render(request, 'articles/detail.html', context)

def update(request,article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        # article = Article.objects.get(pk=article_pk)
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form
    }
    return render(request, 'articles/update.html', context)

def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:detail', article.pk)

def singer(request):

    return render(request, 'articles/singer.html')