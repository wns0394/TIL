from django.urls import path
# 현재 폴더에 있는 views를 가져온다
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    # detail로 가는거는 그 고유 pk가 필요할거같다.
    # detial은 경로로 가는게 아니라 그냥 그 고유값을 가지고해서 경로가 필요없나?
    path('<int:article_pk>/', views.detail, name ='detail'),
    path('update/<int:article_pk>/', views.update, name='update'),
    path('delete/<int:article_pk>/', views.delete, name='delete'),
    # 새로운페이지
    path('singer/', views.singer, name='singer')
]
