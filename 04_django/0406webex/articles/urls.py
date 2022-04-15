from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    # 게시글 생성을 위해 필요한
    # path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    # 수정한다 -> 뭘? 1번 게시글을 수정한다.
    # 무슨 게시글을 수정하는지 알ㄹ주어야한다
    # update/1/ -> 이렇게 오면 그 1이라는 값을 어떤 변수에 담을 것이다.
    path('update/<int:article_pk>', views.update, name='update'),
]