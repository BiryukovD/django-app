from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'user')  # Поля для отображения в списке
    search_fields = ('title', 'author')  # Поля для поиска
    list_filter = ('author', 'published_date')  # Поля для фильтрации

admin.site.register(Book, BookAdmin)
