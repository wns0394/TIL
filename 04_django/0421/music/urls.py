from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    path('artists/', views.artist_list_create, name='artist_list_create'),
    path('artists/<int:artist_pk>/', views.artist_detail, name='artist_detail'),
    path('music/', views.music_list, name='music_list'),
    path('artists/<int:artist_pk>/music/', views.music_create, name='music_create'),
    path('music/<int:music_pk>/', views.music_detail, name='music_detail'),
]