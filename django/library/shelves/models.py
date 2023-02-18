from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)

    @property
    def url_name(self) -> str:
        return f'author_{self.id}'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'


class Publisher(models.Model):
    name = models.CharField(max_length=50)
    authors = models.ManyToManyField(Author)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return f'{self.name}'
