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
        c4 = Category.objects.create(name="Detective")
        c5 = Category.objects.create(name="Fiction")
        c6 = Category.objects.create(name="Heroic")
        
        a1 = Author.objects.create(first_name="Anthony", middle_name="", last_name="Reynolds")
        a2 = Author.objects.create(first_name="Elisabetta", middle_name="", last_name="Dami")
        a3 = Author.objects.create(first_name="Michael", middle_name="", last_name="Ende")
        a4 = Author.objects.create(first_name="Athur", middle_name="Connan", last_name="Doyle")
        a5 = Author.objects.create(first_name="Suzanne", middle_name="", last_name="Collins")
        a6 = Author.objects.create(first_name="Patrick", middle_name="", last_name="Rothfuss")
	 
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

        b4 = Book.objects.create(isbn="9780140437867", name="Sherlock Holmes: The Hound of the Baskerville")
        b4.categories.add(c4)
        b4.categories.add(c5)
        b4.authors.add(a4)
        
        b5 = Book.objects.create(isbn="9789510449622", name="The Ballad of Songbirds and Snakes (A Hunger Games Novel)")
        b5.categories.add(c2)
        b5.categories.add(c3)
        b5.authors.add(a5)
        
        b6 = Book.objects.create(isbn="9783608938166", name="The Wise Man's Fear")
        b6.categories.add(c1)
        b6.categories.add(c6)
        b6.authors.add(a6)
        
        b7 = Book.objects.create(isbn="9788401022524", name="The Name of the Wind")
        b7.categories.add(c1)
        b7.categories.add(c6)
        b7.authors.add(a6)

        c1.save()
        c2.save()
        c3.save()
        c4.save()
        c5.save()
        c6.save()
        
        a1.save()
        a2.save()
        a3.save()
        a4.save()
        a5.save()
        a6.save()
        
        b2.save()
        b3.save()
        b1.save()
        b4.save()
        b5.save()
        b6.save()
        b7.save()

        for book in Book.objects.all():
            for i in range(5):
                PhysicalBook.objects.create(
                    book=book,
                    id=f"{book.isbn}-{i}"
                )

