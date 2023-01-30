from django.http import HttpResponseRedirect
from django.shortcuts import render

from lms.storage.models import Book, Category
import random


def home_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')

    random_category = _random_category()
    books_query = Book.objects.filter(categories=random_category)
    books = list(books_query)

    context = {'books_obj': books[1:4], 'book_ind': books[0], 'category': random_category}
    return render(request, 'index.html', context)  # Fathi view


def _random_category() -> Category:
    while True:
        category = Category.objects.all().order_by("?").first()
        if category.books.count() > 0:
            return category
