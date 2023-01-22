from django.db.models import Model, CharField, ForeignKey, SET_NULL, CASCADE, DateTimeField, ManyToManyField
from django.contrib.auth.models import User

from libraryManagemetSystem.storage.models import Category, Author


class Book(Model):
    isbn = CharField(primary_key=True, unique=True, max_length=256)
    name = CharField(max_length=256)
    categories = ManyToManyField(Category, related_name="books")
    authors = ManyToManyField(Author, related_name="books")


class PhysicalBook(Model):
    book = ForeignKey(Book, related_name="physical_books", on_delete=CASCADE)


class PhysicalBookRentHistory(Model):
    physical_book = ForeignKey(PhysicalBook, related_name="rent_history", on_delete=CASCADE)
    rented_by = ForeignKey(User, on_delete=SET_NULL, null=True, blank=True)
    rented_on = DateTimeField()
    rent_deadline = DateTimeField()
