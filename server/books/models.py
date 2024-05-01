from django.db import models
from django.utils.text import slugify


# Create your models here.
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300)
    author = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=4, decimal_places=2)
    quantity = models.IntegerField()
    picture = models.ImageField(upload_to='images/')
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} | {self.author} | {self.price}"
