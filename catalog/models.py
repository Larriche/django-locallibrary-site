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

