from django.shortcuts import render


def librarian_view(request):
    return render(request, 'library/librarian.html')
