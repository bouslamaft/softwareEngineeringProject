from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render

from lms.storage.models import Book


def list_books_view(request):
    books = Book.objects.all()

    page = request.GET.get('page')
    paginator = Paginator(books, 5)

    try:
        books_obj = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        books_obj = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        books_obj = paginator.page(page)

    context = {'books_obj': books_obj, 'paginator': paginator}
    return render(request, 'listBooks.html', context)
