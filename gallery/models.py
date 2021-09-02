from django.db import models

# Create your models here.

class Images(models.Model):
    image = models.ImageField(upload_to = 'articles/',default='SOME STRING')
    description=models.TextField(max_length=2000)
    