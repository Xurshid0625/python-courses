from django.db import models




class Categories(models.Model):
    name = models.CharField(max_length=255)
    
    
    def __str__(self):
        return self.name
    


class Product(models.Model):
    categories = models.ForeignKey(Categories,null=True,on_delete=models.CASCADE)    
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=255)
    text = models.TextField()
    price = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name