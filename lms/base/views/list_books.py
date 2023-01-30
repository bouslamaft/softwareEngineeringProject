from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from lms.storage.models import Book, PhysicalBook, PhysicalBookRentHistory
from datetime import datetime, timedelta

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
    physicalBook = PhysicalBook.objects.filter(book=book)
    
    count = 0
    
    for i in range(0,   physicalBook.count()):
        if physicalBook[i].is_currently_rented == 0:
            count+=1
    
    context = {'book':book, 'physicalBook': physicalBook, 'amm': count}
    return render(request, 'books/rent.html', context)

def rented_book_view(request, isbn):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')
    book = Book.objects.get(pk=isbn)
    physicalBook = PhysicalBook.objects.filter(book=book)
    current_user = request.user
    current_dateTime = datetime.now()
    deadline_dateTime = current_dateTime + timedelta(days=14)
    
    rent = 0
    for i in range(0,   physicalBook.count()):
        pbrh = PhysicalBookRentHistory.objects.filter(physical_book=physicalBook[i])
        if pbrh.count()==0 and rent==0:
            rent+=1
            pbrh = PhysicalBookRentHistory(rented_by=current_user, physical_book=physicalBook[i],rented_on=current_dateTime, rent_deadline=deadline_dateTime)
            pbrh.save()
    
    return redirect('/listBooks')

def book_view(request, isbn):
    book = Book.objects.get(pk=isbn)
    context = {'book':book}
    return render(request, 'books/book.html', context)
