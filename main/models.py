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
    
class New(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField()
    image = models.ImageField(upload_to='images/')
    data = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    
class Video(models.Model):
    
    name = models.CharField(max_length=255)
    video = models.FileField(upload_to='videos/')
    
    def __str__(self):
        return self.name