from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render

from lms.storage.models import Book


def list_books_view(request):
    books = Book.objects.all()

    filterData = request.GET.get('filter', None)
    
    if(filterData=='isbn'):
        books = Book.objects.all().order_by('-isbn')
    elif(filterData!='title'):
        books = Book.objects.all().order_by('name')
    elif(filterData!='author'):
        books = Book.objects.all().order_by('-authors')
    elif(filterData!='category'):
        books = Book.objects.all().order_by('-categories')
    else:
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

    context = {'books_obj': books_obj, 'paginator': paginator, 'filteredData': filterData}
    return render(request, 'books/listBooks.html', context)


def rent_view(request, isbn):
    book = Book.objects.get(pk=isbn)
    context = {'book':book}
    return render(request, 'books/rent.html', context)

def book_view(request, isbn):
    book = Book.objects.get(pk=isbn)
    context = {'book':book}
    return render(request, 'books/book.html', context)
