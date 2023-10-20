from django.db import models
from django.utils.text import slugify

# Create your models here.

class Iexcel_Blog(models.Model):
    author = models.CharField(max_length=50)
    date = models.DateField()
    title = models.CharField(max_length=120)
    extract = models.CharField(max_length=255)
    content = models.TextField(max_length=1024)
    image = models.ImageField(default='')
    slug = models.SlugField(default='')

    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


    def __str__(self):
        return f"'{self.title}' '{self.image}' '{self.extract}' '{self.content}'"