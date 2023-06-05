from datetime import date
from django.db import models


# Create your models here.

class Student(models.Model):
    id =models.IntegerField(primary_key=True)
    first_name =models.CharField(max_length=20, null =True, blank=True)
    last_name =models.CharField(max_length=20, null=True, blank=True)
    dob =models.DateField(null=True, blank=True)
    
    DisplayFields=['id', 'first_name', 'last_name', 'dob', 'age']
    SearchableFields =['first_name', 'last_name']
    FilterFields =['dob']
    # Renaming a table    
    class Meta:
        db_table ='STUDENT'
    #   add a calculated field in the models  
    @property
    def age(self):
        if(self.dob != None):
            age =date.today().year - self.dob.year
            return age
        