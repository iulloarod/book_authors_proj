from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    #authors: es una lista de autores asociados a un libro 

    def __repr__(self) -> str:
        return f"Book titled {self.title}. {self.desc}"


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    books = models.ManyToManyField(Book, related_name="authors")
    notas = models.TextField(null=True)

    def __repr__(self) -> str:
        return f"Author {self.first_name} {self.last_name}"