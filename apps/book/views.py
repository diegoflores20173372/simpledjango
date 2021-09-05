from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import AuthorForm
from .models import Author


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
    return render(request, 'book/create_author.html', {'author_form': author_form})


def listAuthor(request):
    authors = Author.objects.filter(state=True)
    return render(request, 'book\list_author.html', {'authors': authors})


def editAuthor(request, id):
    author_form = None
    error = None
    try:
        author = Author.objects.get(id=id)
        if request.method == 'GET':
            author_form = AuthorForm(instance=author)
        else:
            author_form = AuthorForm(request.POST, instance=author)
            if author_form.is_valid():
                author_form.save()
            return redirect('index')
    except ObjectDoesNotExist as e:
        error = e

    return render(request, 'book\create_author.html', {'author_form': author_form, 'error': error})


def deleteAuthor(request, id):
    author = Author.objects.get(id=id)
    if request.method == 'POST':
        author.state = False
        author.save()
        return redirect('book:List_Author')
    return render(request, 'book/delete_author.html', {'author': author})



