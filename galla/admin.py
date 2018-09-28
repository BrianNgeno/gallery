from django.contrib import admin
from .models import Editor,Categorys,Image,Location


# Register your models here.

class ImageAdmin(admin.ModelAdmin):
    filter_horizontal = ('Categorys')
    
admin.site.register(Editor)
admin.site.register(Categorys)
admin.site.register(Image,ImageAdmin)
admin.site.register(Location)
