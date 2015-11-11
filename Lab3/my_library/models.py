from django.db import models

class Book(models.Model):
    ISBN = models.CharField(max_length=50)
    Title = models.CharField(max_length=60)
    AuthorID = models.CharField(max_length=50)
    Publisher = models.CharField(max_length=50)
    PublishDate = models.CharField(max_length=20)
    Price = models.CharField(max_length=20)
class Author(models.Model):
    AuthorID = models.CharField(max_length=30)
    Name = models.CharField(max_length=50)
    Age = models.CharField(max_length=10)
    Country = models.CharField(max_length=20)
