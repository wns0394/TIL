from django.shortcuts import redirect, render, get_object_or_404
from .models import Either
from .forms import EitherForm
# Create your views here.

def index(request):
    eithers = Either.objects.all()
    context = {
        'eithers':eithers,
    }
    return render(request, 'eithers/index.html', context)


def create(request):
    if request.method == 'POST':
        form = EitherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('eithers:index')
    else:
        form = EitherForm()
    context = {
        'form': form,
    }
    return render(request, 'eithers/create.html', context)

def detail(request, article_pk):
    either = get_object_or_404(Either, pk=article_pk)
    context = {
        'either':either,
    }
    return render(request,'eithers/detail.html',context)