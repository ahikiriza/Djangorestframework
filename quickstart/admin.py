from django.contrib import admin
# from .models import *
from .models import Student
# Register your models here.
# admin.site.register(Student)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display =Student.DisplayFields
    search_fields =Student.SearchableFields
    list_filter =Student.FilterFields
