from django.db import models

# Create your models here
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='book_app/images/')

    def __str__(self):
        return self.title

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    review = models.TextField(max_length=500)
    rating = models.IntegerField()
    reviewer = models.CharField(max_length=50)

    def __str__(self):
        return self.reviewer  