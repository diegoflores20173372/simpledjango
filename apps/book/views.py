from django.shortcuts import render
from .forms import AuthorForm


# Create your views here.


def Home(request):
    return render(request, 'index.html')


def createAuthor(request):
    if request.method == 'POST':
        author_form = AuthorForm(request.POST)
        if author_form.is_valid():
            author_form.save()
