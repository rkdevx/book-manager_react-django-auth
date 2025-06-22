from django.db import models

# Create your models here.

class Book(models.Model):
    id = models.BigAutoField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField(default="No description yet")
    published_date = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'book'

    def __str__(self):
        return self.title
