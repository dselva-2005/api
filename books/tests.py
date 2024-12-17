from django.test import TestCase
from .models import Book
from django.urls import reverse


# Create your tests here.
class BookTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title="The rust book",
            subtitle="excellent book to learn rust",
            author="Dselva",
            isbn="3203909239424",
        )

    def test_book_content(self):
        self.assertEqual(self.book.title, "The rust book")
        self.assertEqual(self.book.subtitle, "excellent book to learn rust")
        self.assertEqual(self.book.author, "Dselva")
        self.assertEqual(self.book.isbn, "3203909239424")

    def test_book_listview(self):
        response = self.client.get(reverse("book_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Dselva")
        self.assertTemplateUsed(response, "books/book_list.html")
