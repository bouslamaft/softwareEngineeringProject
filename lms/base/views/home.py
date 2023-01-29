from django.http import HttpResponseRedirect
from django.shortcuts import render

from lms.storage.models import Book, Category
import random

def home_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')

    # return render(request, 'index.html')  # Fathi view
    #if request.user.is_authenticated:
    #    return HttpResponseRedirect('afterlogin')
    # return render(request,'index.html')
    
    categories = Category.objects.all()
    
    rngVariable = random.randint(0, categories.count()-1)
    
    filterValue = categories[rngVariable]
    
    books = Book.objects.filter(categories=filterValue)
    
    context = {'books_obj': books[1:], 'book_ind':books[0], 'category': filterValue}
    return render(request, 'index.html', context)  # Fathi view
