from django.shortcuts import render, redirect, get_object_or_404
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

# 이제 필요없다
# def new(request):
#     return render(request, 'articles/new.html')

def create(request):
    # 사용자가 POST 요청을 보냈다면...
    if request.method == 'POST':
        # GET 요청으로 보내진 데이터는
        # title = request.GET.get('title') # QueryDict
        # content = request.GET.get('content')
        title = request.POST.get('title') # QueryDict
        content = request.POST.get('content')

        '''
        Article.objects.create(title=title, content=content)
        '''

        article = Article()
        article.title = title
        article.content = content
        # db에 반영할
        article.save()

        #POST 요청에 맞게 게시글을 생성하고 난 후
        # 경로가 수정 될 경우 redirect에 작성한 경로도 수정해야한다.

        # detail 페이지는 article_pk를 필요로 한다. 이거는 어디에 있나 바로위에 article.save()에 들어가있지
        # redirect는 함수다 고로 ,가 필요하다
        return redirect('articles:detail', article.pk)
    # 아니면??
    # else:
        # GET 요청이 왔으니 html 문서를 보여주자....
        # 근데 뭘 보여줘야하지??
        # 이거는 안된다 index페이지에는 모든 정보가 다 있어야하니까 ---> 이해못함
        # return render(request, 'articles/index.html')
    # return render(request, 'articles/create.html')
    return render(request, 'articles/form.html')

def detail(request, article_pk):
    # article_pk 번째 게시글의 정보를 조회, 반영
    # article = Article.objects.get(pk=article_pk)
    # 위에랑 아래 차이 기억해두기 위에는 이미 Article의 정보가 있다
    # 아래에는 그런 정보가 없으므로 Article을 적어주고 거기서 조건인 pk=article_pk를 적어주어야한다
    article = get_object_or_404(Article, pk=article_pk)

    context = {
        'article' : article
    }
    return render(request, 'articles/detail.html', context)
def delete(request, article_pk):
    # 특정 게시글 조회
    # article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        article = get_object_or_404(Article, pk=article_pk)
        article.delete()

    return redirect('articles:index')

def update(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect('articles:detail', article.pk)
    else:
        context = {
            'article' : article
        }
    # return render(request, 'articles/update.html', context)
    return render(request, 'articles/form.html', context)