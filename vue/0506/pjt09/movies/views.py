from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.views.decorators.http import require_safe
from .models import Movie
from django.core.paginator import Paginator
# Create your views here.
@require_safe
def index(request):
    movies = get_list_or_404(Movie)
    paginator = Paginator(movies,10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'movies' : page_obj
    }
    return render(request, 'movies/index.html', context)


@require_safe
def detail(request, movie_pk):
    pass


@require_safe
def recommended(request):
    pass