### Workshop 진행과정

1. vscode에서 가상환경 만들고 켜주기

​	`python -m venv venv` : 가상환경 만들기

​	`source venv/Script/activate` : 가상환경 키기

2. `pip list` 확인 후 필요한 것들 설치해주기

​	`python manage.py -r requirements.txt` 

3. 프로젝트, 앱 생성

​	`django-admin startproject crud .` : 프로젝트 생성

​	`python manage.py startapp articles` : 앱 생성

4. settings.py에 installed_app에 'articles', 추가해주기
5. 프로젝트의 urls.py에 설정해주기

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # articles/ 뒤에 오는 경로들은 artilces가 가지고있는 urls.py를 따른다.
    path('articles/', include('articles.urls')),
]
```

6. 앱에 urls.py 생성후 설정해주기 

```python
from django.urls import path
# 현재 폴더에 있는 views를 가져온다
from . import views

app_name = 'articles'
urlpatterns = [
    # articles/ 뒤에 빈 문자열을 index로 
    path('', views.index, name='index'),
]
```

7. views.py에 index함수 만들어주기

```python
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }

    return render(request, 'articles/index.html',context)
```

8. index.html을 생성하기 위해서 articles에 templates 폴더를 생성하고 그 안에 다시 articles 폴더를 생성하고 그 안에 index.html 생성
9. 우리는  상속받아서 사용할 base.html을 사용할것이므로 앱과 프로젝트랑 동일선상에 templates 폴더를 만들고 그안에 base.html 생성후 body에 blcok content 만들어주기
10. 상속받아서 쓰기 위해서는 settings.py에 TEMPLATES에 설정해주어야한다.

```PYTHON
TEMPLATES = [
    {
        ....
        'DIRS': [BASE_DIR / 'templates',],
        .....
```

11. 이제 index.html을 사용하기 위해서 상속을 받아온다. `{% extends 'base.html' %}` 하고 

​		blcok content 안에 내용을 사용해준다.

12.  index.html 안에 내용을 넣기 위해서 우리는 models.py를 설정해주어야한다.

```python
from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
```

13. `python manage.py makemigrations`, `python manage.py migrate` 해준다.

12.  index.html에서 **우리는 articles 안에 article들 각각에대한 ** 제목 내용 생성일 수정일을 보고싶기에 **for문을 사용한다** 그리고 제목 밑에 생성을 위한 create페이지로 넘어가기 위해서 a태그를 작성하는데 경로를 url로 작성한다.





##### 근데 디테일할때는 `path('<int:article_pk>/', views.detail, name='detail')`로 만드는데 

딜리트 페이지는 왜 `path('<int:article_pk>/', views.detail, name='detail')`로 못만드느냐????

이렇게 만들면 위에 있는거 먼저 찾아서 실행하기 때문에 detail만 실행된다고 생각한다



`{% load static %}` 은 각 html마다 다 써야한다 

그리고 settings.py에 

`STATIC_URL = '/css/'` 로 바꾸어주고 articles에 static폴더 만들어주고 거기에 

그리고 base.html head끝에 block style만들어준다



그리고 또하나 article에 static을 만드는게 아니라 base에 만드렁 주려면 우리가 templastes에 BASE_DIR한거처럼

settings.py에

```python
STATIC_URL = '/css/'   # <- 얘는 원래 있던거 밑에가 새로 적어준거
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
```

를 적어주어야한다

html에 각각

load static해주고 

```python
{ block style}
	<link rel = "stylesheet" href="{% static 'index.css' %}">
end block style
```

