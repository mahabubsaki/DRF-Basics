from django.contrib import admin
from app.models import BookStoreModel

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    pass

admin.site.register(BookStoreModel,BookAdmin)
