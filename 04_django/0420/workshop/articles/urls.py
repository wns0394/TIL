from django.urls import path
from . import views

# app_name 필요없다 이제

urlpatterns = [
    path('articles/', views.article_list),
    path('articles/<int:article_pk>/', views.article_detail),
]
