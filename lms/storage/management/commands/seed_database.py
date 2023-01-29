from django.core.management.base import BaseCommand
from lms.storage.models import Book
from lms.storage.models import Author
from lms.storage.models import PhysicalBook
from lms.storage.models import PhysicalBookRentHistory
from lms.storage.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        c1 = Category.objects.create(name="Fantasy")
        c2 = Category.objects.create(name="Sci-fi")
        c3 = Category.objects.create(name="Adventure")

        a1 = Author.objects.create(first_name="Anthony", middle_name="", last_name="Reynolds")
        a2 = Author.objects.create(first_name="Elisabetta", middle_name="", last_name="Dami")
        a3 = Author.objects.create(first_name="Michael", middle_name="", last_name="Ende")

        b1 = Book.objects.create(isbn="9780525457589", name="The NeverEnd Story")
        b1.categories.add(c1)
        b1.authors.add(a3)

        b2 = Book.objects.create(isbn="9783426228036", name="Ruination")
        b2.categories.add(c1)
        b2.authors.add(a2)

        b3 = Book.objects.create(isbn="9788856628470", name="Geronimo Stilton, The phoenix of destiny")
        b3.categories.add(c1)
        b3.categories.add(c3)
        b3.authors.add(a1)

        c1.save()
        c2.save()
        c3.save()

        a1.save()
        a2.save()
        a3.save()

        b2.save()
        b3.save()
        b1.save()

        for book in Book.objects.all():
            for i in range(5):
                PhysicalBook.objects.create(
                    book=book,
                    id=f"{book.isbn}-{i}"
                )

