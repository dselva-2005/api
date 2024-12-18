from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from books.models import Book


class APITests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title="The python book",
            subtitle="this is a professional book on python",
            author="Dselva",
            isbn="1234567891023",
        )

    def test_api_listiew(self):
        response = self.client.get(reverse("book_list"))
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(Book.objects.count(),1)
        self.assertContains(response,self.book)