from django.contrib import admin

from .models import Author, Genre, Book, BookInstance, Language

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')

# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstance(admin.ModelAdmin):
    list_display = ('status', 'due_back')
    list_filter = ('status', 'due_back')

    fieldsets = (
        ('Book Details', {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )

admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)
admin.site.register(Language)


# Register your models here.
