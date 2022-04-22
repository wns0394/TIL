# 진행 과정



###  1. 가상환경 생성 및 활성화, `pip install -r requirements.txt`

###  2. my_api project 생성 articles 앱 생성

- ### `django-admin startproject my_api .`

- ### `python manage.py startapp articles`

### 3. settings.py에 설정해주기

```python
INSTALLED_APPS = [
    'articles',
    'django_extenstions',
    'djangorestframework',
```

### 틀렸다 이게 아니구나 requirements.txt 에 djangorestframework라고 적혀있길래 그대로 따라쳤는데 rest_framework이다 그리고 django_seed 도 안적어줬다.

```python
INSTALLED_APPS = [
    'articles',
    'django_seed',
    'django_extenstions',
    'rest_framework',
```



### 4. my_api.urls에 경로 작성해주기

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('articles.urls')),
]
```

### 5. articles에 urls.py 생성 후 작성 

```python
from django.urls import path
from . import views

# app_name 필요없다 이제

urlpatterns = [
    path('articles/', views.article_list),
]

```

### 6. models.py 작성

```python
from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

### 7. views.py에서 작성중 명세서의 - GET api/v1/articles/  • 모든 게시글의 id와 title 컬럼을 JSON 데이터 타입으로 응답한다. 를 보고 serializers.py를 만들어야 겠다고 생각 하는김에  명세서의

```python
2. serializers
- ArticleListSerializer 
• 모든 게시글 정보를 반환하기 위한 ModelSerializer 
• Id, title 필드 정의 

- ArticleSerializer 
• 게시글 상세 정보를 반환 및 생성하기 위한 ModelSerializer
• 모든 필드 정의 
요것도 다 작성해주기
```



### 8. articles에 serializers.py 생성후 작성

```python
from rest_framework import serializers
from .models import Article

class ArticleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id', 'title',)


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = '__all__'
```

### 9. 다시 views.py로 돌아와서 import 해줄것들 다 import 해주고 article_list 함수 작성해주기 아래는 스스로 작성해본거 

```PYTHON
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ArticleListSerializer
from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Article
# Create your views here.

@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleListSerializer(articles, many=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
```

- ### 처음에는 many=True 속성을 작성해주지 않았다. 그리고 status를 사용하지 않았다...

- ### 이렇게 작성하니 GET요청을 보낼때는 문제가 없었다. 하지만!!!!!!!

- ### POST요청을 보냈을때 문제가 생겼는데 생성을 한다는것은 단일 인스턴스 이므로 many 옵션이 필요하지 않다 그것만 지운다면 문제 없이 생성 가능하다.



### 10. 이제 명세에 있는

```
 GET api/v1/articles/<article_pk>/ 
• 특정 게시글의 모든 컬럼을 JSON 데이터 타입으로 응답한다.
- PUT & DELETE api/v1/articles/<article_pk>/ 
• PUT 요청인 경우 특정 게시글의 정보를 수정한다.
▪ 검증에 성공하는 경우 수정된 게시글의 정보를 DB에 저장한다.
▪ 검증에 실패할 경우 400 Bad Request 예외를 발생시킨다.
▪ 수정이 완료되면 수정한 게시글의 정보를 응답한다.
• DELETE 요청인 경우 특정 게시글을 삭제한다.
▪ 삭제가 완료되면 삭제한 게시글의 id를 응답한다.
```

### 이 친구들 만들어 주자
