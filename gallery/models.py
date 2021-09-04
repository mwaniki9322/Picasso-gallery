from django.db import models

# Create your models here.

class Images(models.Model):
    image_name=models.CharField(max_length=70)
    description=models.TextField(max_length=2000)
    
    def __str__(self):
        return self.image_name

class Location(models.Model):
    location=models.TextField(max_length=100)

    def __str__(self):
        return self.location

class Category(models.Model):
    category = models.CharField(max_length =30)

    def __str__(self):
        return self.category