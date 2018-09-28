from django.contrib import admin
from .models import Editor,Categorys,Image,Location


# Register your models here.

# class ImageAdmin(admin.ModelAdmin):
#     filter_horizontal = ('Category',)

admin.site.register(Editor)
admin.site.register(Image)
admin.site.register(Location)
admin.site.register(Categorys)
