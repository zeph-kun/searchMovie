from django.db import models

# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=100)
    year = models.CharField(max_length=4, null=True, blank=True)
    type = models.CharField(null=True, blank=True, max_length=20)

    @staticmethod
    def format_year(year):
        return year.split('-')[0] if '-' in year else year

    def __str__(self):
        return f"{self.title} ({self.year})"