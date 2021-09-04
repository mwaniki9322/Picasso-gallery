from django.db import models


#create models here

class Locations(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

    
    def save_location(self):
        self.save()
    
    def delete_location(self):
        self.delete()



class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()
     
class Image(models.Model):
    image_name=models.CharField(max_length=100)
    image_description=models.TextField(max_length=300)
    location=models.ForeignKey(Locations,on_delete=models.CASCADE)
    Category=models.ForeignKey(Category,on_delete=models.CASCADE)

    def save_image(self):
        self.save()

    
        