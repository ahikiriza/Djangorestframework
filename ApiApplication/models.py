from django.db import models

# Create your models here.
class Book(models.Model):
    id =models.IntegerField(primary_key=True)
    title =models.CharField(max_length=200)
    author =models.CharField(max_length=200)
    DisplayFields=['id', 'title','author']
    SearchableFields=['id','title', 'author']
    
    
    
class Student(models.Model):
    id =models.IntegerField(primary_key=True)
    first_name =models.CharField(max_length =20)
    last_name =models.CharField(max_length =20, blank=True, null=True)
    dob =models.DateField(null=True, blank=True)