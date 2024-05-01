from django.db import models


# Create your models here.
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300)
    author = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=4, decimal_places=2)
    quantity = models.IntegerField()
    picture = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"{self.name} | {self.author} | {self.price}"
