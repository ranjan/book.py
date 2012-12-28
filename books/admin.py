from django.contrib import admin
from demoapp.books.models import Author
from demoapp.books.models import Book
from demoapp.books.models import Publisher

class AuthorAdmin(admin.ModelAdmin):
  list_display = ('first_name', 'last_name', 'email')
  search_fields = ('first_name', 'last_name')
class BookAdmin(admin.ModelAdmin):
  list_display = ('title', 'publisher', 'publication_date')
  list_filter = ('publication_date',)

admin.site.register(Publisher)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)