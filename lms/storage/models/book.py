import datetime

from django.db.models import Model, CharField, ForeignKey, SET_NULL, CASCADE, DateTimeField, ManyToManyField
from django.contrib.auth.models import User

from lms.storage.models import Category, Author


class Book(Model):
    isbn = CharField(primary_key=True, unique=True, max_length=256)
    name = CharField(max_length=256)
    categories = ManyToManyField(Category, related_name="books")
    authors = ManyToManyField(Author, related_name="books")

    def __str__(self):
        return f"Book({self.name})"


class PhysicalBook(Model):
    id = CharField(primary_key=True, max_length=256)
    book = ForeignKey(Book, related_name="physical_books", on_delete=CASCADE)

    @property
    def is_currently_rented(self):
        now = datetime.datetime.now()
        n = self.rent_history.all().filter(rent_deadline__gte=now).filter(rented_on__lte=now).count()

        return n != 0
    @property
    def current_rent_history(self):
        now = datetime.datetime.now()
        n = self.rent_history.all().filter(rent_deadline__gte=now).filter(rented_on__lte=now).first()

        return n 
    


class PhysicalBookRentHistory(Model):
    physical_book = ForeignKey(PhysicalBook, related_name="rent_history", on_delete=CASCADE)
    rented_by = ForeignKey(User, on_delete=SET_NULL, null=True, blank=True)
    rented_on = DateTimeField()
    rent_deadline = DateTimeField()
