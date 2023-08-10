from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    is_borrowed = models.BooleanField(default=False)
    borrowed_date = models.DateField(null=True, blank=True)

class User(models.Model):
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    borrowed_book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True, blank=True)
