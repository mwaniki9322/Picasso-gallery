from django.db import models

# Create your models here.

class Images(models.Model):
    image_name=models.CharField(max_length=70)
    description=models.TextField(max_length=2000)
