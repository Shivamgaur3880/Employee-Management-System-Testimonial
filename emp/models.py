from django.db import models

# Create your models here.

class employee(models.Model):
    name = models.CharField(max_length=50)
    emp_id = models.CharField(max_length=50)
    phone = models.CharField( max_length=50)
    address = models.CharField( max_length=50)
    working = models.BooleanField(default= True)
    department = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class testimonial(models.Model):
    name= models.CharField(max_length=50)
    testimonial = models.TextField()
    picture= models.ImageField(upload_to = "testimonial/")
    rating= models.IntegerField(max_length=1)

    def __str__(self):
        return self.testimonial
        