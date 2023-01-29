from django.http import HttpResponseRedirect
from django.shortcuts import render

from lms.storage.models import Book
def home_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')

    return render(request, 'index.html')  # Fathi view
    #if request.user.is_authenticated:
    #    return HttpResponseRedirect('afterlogin')
    # return render(request,'index.html')
    books = Book.objects.all()
    context = {'books_obj': books, 'book_ind':books[0]}
    return render(request, 'index.html', context)  # Fathi view
