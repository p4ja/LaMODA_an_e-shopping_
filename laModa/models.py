from django.db import models

# Create your models here.
class category_db(models.Model):
    CategoryName=models.CharField(max_length=100,null=True,blank=True)
    Description=models.TextField(max_length=100,null=True,blank=True)
    Imageupload=models.ImageField(upload_to="Imageupload",null=True,blank=True)

class product_db(models.Model):
    ProductName=models.CharField(max_length=100,null=True,blank=True)
    ProductCategory=models.CharField(max_length=100,null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    Price=models.IntegerField(null=True,blank=True)
    ProductImage=models.ImageField(upload_to="ProductImage",null=True,blank=True)
