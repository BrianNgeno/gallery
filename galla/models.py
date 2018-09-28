from django.db import models
import datetime as dt

# Create your models here.
class Editor(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()


    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ['first_name']

class Categorys(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name



class Location(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Image(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    location = models.ForeignKey(Location)
    category = models.ManyToManyField(Categorys, default = True)
    pub_date = models.DateTimeField(auto_now_add=True, null=True)
    Image_image = models.ImageField(upload_to = 'images/')
