from datetime import date

from django.test import TestCase
from freezegun import freeze_time

from lms.storage.models import PhysicalBook, PhysicalBookRentHistory, Book
from django.contrib.auth.models import User


class PhysicalBookTestCase(TestCase):

    @freeze_time(date(year=2023, month=1, day=1))
    def test_is_currently_rented_happy_path(self):
        b = Book.objects.create(isbn="1", name="Harry Potter 1")
        physical_book = PhysicalBook.objects.create(book=b, id="1-1")
        rent = PhysicalBookRentHistory.objects.create(
            physical_book=physical_book,
            rented_by=None,
            rented_on=date(year=2022, month=12, day=30),
            rent_deadline=date(year=2023, month=2, day=1)
        )

        self.assertTrue(physical_book.is_currently_rented)

    @freeze_time(date(year=2023, month=1, day=1))
    def test_is_currently_rented_returns_false_when_past_history_present(self):
        b = Book.objects.create(isbn="1", name="Harry Potter 1")
        physical_book = PhysicalBook.objects.create(book=b, id="1-1")
        rent = PhysicalBookRentHistory.objects.create(
            physical_book=physical_book,
            rented_by=None,
            rented_on=date(year=2022, month=10, day=1),
            rent_deadline=date(year=2022, month=10, day=15)
        )

        self.assertFalse(physical_book.is_currently_rented)

    @freeze_time(date(year=2023, month=1, day=1))
    def test_is_currently_rented_returns_false_when_no_history(self):
        b = Book.objects.create(isbn="1", name="Harry Potter 1")
        physical_book = PhysicalBook.objects.create(book=b, id="1-1")
        self.assertFalse(physical_book.is_currently_rented)


class LoginViewTest(TestCase):
    def test_logging_in_with_real_credentials_redirects_on_success_and_sets_cookie(self):
        user = User.objects.create_user(username="john", email="john@example.com", password="john")

        response = self.client.post("/login/", {"username": user.username, "password": "john"})

        self.assertEqual(response.status_code // 100, 3)
        self.assertIsNotNone(self.client.cookies["sessionid"])

    def test_logging_in_with_invalid_credentials_returns_a_message_in_the_html(self):
        User.objects.create_user(username="john", email="john@example.com", password="john")

        response = self.client.post("/login/", {"username": "aaaaaaaaaaaaaaaaaa", "password": "blablabal"})

        self.assertIn("Invalid credentials please try again", response.content.decode("ascii"))

    def test_register_view_creates_a_user(self):
        r = self.client.post("/registration/", {
            "username": "xd",
            "email": "xd@example.com",
            "password": "password"
        })

        self.assertEqual(User.objects.count(), 1)


class RentBookTest(TestCase):
    def test_try_to_rent_book_not_logged_in(self):
        b = Book.objects.create(isbn="1", name="Harry Potter 1")
        response = self.client.post("/rentedBook/"+b.isbn)
        self.assertEquals(response.status_code, 302)
        
        response = self.client.post("/rentedBook/"+b.isbn, follow=True)
        self.assertIn("Login", response.content.decode("ascii"))
        
    def test_try_to_rent_book_logged_in(self):
        user = User.objects.create_user(username="john", email="john@example.com", password="john")
        response = self.client.post("/login/", {"username": user.username, "password": "john"})
        
        b = Book.objects.create(isbn="1", name="Harry Potter 1")
        
        response = self.client.post("/rentedBook/"+b.isbn, follow=True)
        self.assertIn("All Books", response.content.decode("ascii"))
