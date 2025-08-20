from django.contrib import admin
from .models import Library, Book, Author


admin.site.register(Library)
admin.site.register(Book)
admin.site.register(Author)
