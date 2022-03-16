from django.urls import path
from . import views


# namespace
app_name = 'articles'

urlpatterns = [
    # articles/ 생략된 상태
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
]