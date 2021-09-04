from django.db import models

#create models here

class Image(models.Model):
    name = models.CharField(max_length =30)
    description = models.CharField(max_length =300)

    def __str__(self):
            return self.name

class locationss(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name
    


