from django.db import models

# Create your models here.
class Genre(models.Model):
    """Model representing a book genre."""
    name = models.CharField(max_length=200, help_text="Enter a book genre (eg.Science Fiction")

    def __str__(self):
        """String for representing the Model object"""
        return self.name

class Language(models.Model):
    """
    Model representing a Language (eg. English, French, etc)
    """
    name = models.CharField(max_length=200, help_text="Enter the book's natural language (eg. English, French")

    def __str__(self):
        """
        String for representing a Language
        """
        return self.name

class Book(models.Model):
    """Model representing a book (but not a specfic copy of a book). """
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    isbn = models.CharField('ISBN', max_length=13,
        help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book');
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """String representing the Model object"""
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('book-detail', args=[str(self.id)])


