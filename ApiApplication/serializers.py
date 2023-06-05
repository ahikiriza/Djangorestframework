from rest_framework import serializers
from .models import *

class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =Book
        fields =['id', 'title', 'author']
    id =serializers.IntegerField(label ="Enter Book Id")
    title =serializers.CharField(label ="Enter Book title")
    author =serializers.CharField(label ="Enter author label")
    
    
    
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model =Student
        fields =['id', 'first_name', 'last_name', 'dob']