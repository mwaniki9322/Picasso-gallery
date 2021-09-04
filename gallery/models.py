from django.db import models

#create models here

class Image(models.Model):
    name = models.CharField(max_length =30)
    description = models.CharField(max_length =300)
    


