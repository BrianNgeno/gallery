from django.db import models
import datetime as dt

# Create your models here.
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

    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def gallery_images(cls):
        galla = cls.objects.all()
        return galla

    @classmethod
    def search_by_category(cls,search_term):
        galla = cls.objects.filter(category__name__icontains=search_term)
        return galla

    @classmethod
    def get_by_location(cls,search_term):
        galla = cls.objects.filter(location_name_icontains=search_term)
        return galla