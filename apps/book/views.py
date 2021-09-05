from django.shortcuts import render, redirect
from .forms import AuthorForm


# Create your views here.


def Home(request):
    return render(request, 'index.html')


def createAuthor(request):
    if request.method == 'POST':
        author_form = AuthorForm(request.POST)
        if author_form.is_valid():
            author_form.save()
            return redirect('index')
    else:
        author_form = AuthorForm()
        # print(author_form)
    return render(request, 'book/create_author.html', {'author_form': author_form})
