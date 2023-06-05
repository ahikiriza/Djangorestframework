from django.contrib import admin
from .models import Book
from .models import *
# Register your models here.
# admin.site.register(Book)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display =Book.DisplayFields
    search_fields =Book.SearchableFields
    # list_filter =Student.FilterFields