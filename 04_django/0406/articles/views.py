from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from .models import Article
from .forms import ArticleForm

# Create your views here.
@require_safe
def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


# def new(request):
    # new페이지에서 제출하면 GET이 뜬다
    # print(request.method)
    # form = ArticleForm()
    # context = {
    #     'form': form,
    # }
    # return render(request, 'articles/new.html', context)

@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        # create
        form = ArticleForm(request.POST)
        # 유효성 검사
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
        # print(form.errors)
    else:
        # new
        form = ArticleForm()
    # 위에 유효성 검사에서 통과하지 못하면 context에 갈곳이 없으므로 앞으로 땡겨주어야한다
    # 중요
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)
        

    # form = ArticleForm(request.POST)
    # # 유효성 검사
    # if form.is_valid():
    #     article = form.save()
    #     return redirect('articles:detail', article.pk)
    # # 관리자 권한으로 10자제한을 지우고 10자이상적고 제출하니 is_valid에 걸려서 new로 간다
    # print(form.errors)
    # return redirect('articles:new')

    # title = request.POST.get('title')
    # content = request.POST.get('content')

    # article = Article(title=title, content=content)
    # article.save()

    # return redirect('articles:detail', article.pk)

@require_safe
def detail(request, pk):
    # article = Article.objects.get(pk=pk)
    article = get_object_or_404(Article, pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

@require_POST
def delete(request, pk):
    # article = Article.objects.get(pk=pk)
    article = get_object_or_404(Article, pk=pk)
    # if request.method == 'POST':
    #     article.delete()
    #     return redirect('articles:index')
    # else:
    #     return redirect('articles:detail', article.pk)
    article.save()
    return redirect('articles:index')


# def edit(request, pk):
#     article = Article.objects.get(pk=pk)
#     context = {
#         'article': article,
#     }
    # return render(request, 'articles/edit.html', context)

@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        # article = Article.objects.get(pk=pk)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        # article = Article.objects.get(pk=pk)
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)

    # article = Article.objects.get(pk=pk)
    # article.title = request.POST.get('title')
    # article.content = request.POST.get('content')
    # article.save()
    # return redirect('articles:detail', article.pk)
