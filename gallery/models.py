from django.db import models


#create models here

class Locations(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

    
    def save_location(self):
        self.save()

class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
     
class Image(models.Model):
    image_name=models.CharField(max_length=100)
    image_description=models.TextField(max_length=300)
    location=models.ForeignKey(Locations,on_delete=models.CASCADE)
    Category=models.ForeignKey(Category,on_delete=models.CASCADE)

