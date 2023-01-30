from django.shortcuts import render
from lms.storage.models import PhysicalBook


def student_view(request):
    rented_books = []
    for pyh_books in PhysicalBook.objects.all():
        if pyh_books.is_currently_rented and pyh_books.current_rent_history.rented_by == request.user:
            rented_books.append(pyh_books)
    
    #print(rented_books)
    context = { 'books': rented_books}


    return render(request, 'library/student.html', context)
