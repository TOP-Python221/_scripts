from django.shortcuts import render

from shelves.models import Author, Book, Publisher


def index_view(request):
    return render(
        request,
        'shelves/index.html',
        {
            'authors': Author.objects.all(),
            'publishers': Publisher.objects.all(),
        }
    )


def author_view(request, author_id: int):
    author = Author.objects.get(pk=author_id)
    return render(
        request,
        'shelves/author.html',
        {
            'author': author,
            'books': Book.objects.filter(author=author)
        }
    )


def publisher_view(request):
    pass

