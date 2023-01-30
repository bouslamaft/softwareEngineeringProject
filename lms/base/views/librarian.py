from django.shortcuts import render
from lms.storage.models import PhysicalBook

def librarian_view(request):
    rented_books = []
    for pyh_books in PhysicalBook.objects.all():
        if pyh_books.is_currently_rented:
            rented_books.append(pyh_books)
    
    #print(rented_books)
    context = { 'ibs_obj': rented_books}
    return render(request, 'library/librarian.html' , context)
