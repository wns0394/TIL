from django.urls import path
# 단, django에서는 명시ㅣ적 경로를 작성해 주어야 한다.
# from . -> 현재 파일에 있는 views파일을 가져오겠다
from . import views

app_name = 'articles'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    path('random-user/', views.randomuser, name='randomuser'),
    # < datatype : variable_name >
    # name = ' 배준식 '
    path('hello/<str:name>/', views.hello, name='hello'),
]