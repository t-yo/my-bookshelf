from django.db import models

# Create your models here.



class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=255)
    publication_date = models.DateField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=255)
    comment = models.TextField()
    rate = models.IntegerField()  # add constraints for the rating range

    def __str__(self):
        return f"Review for {self.book.name} by {self.user_name}"