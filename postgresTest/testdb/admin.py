from django.contrib import admin

# Register your models here.
from .models import Person


class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'date_of_birth', 'country_of_birth', 'gender')
    search_fields = ('first_name', 'last_name','country_of_birth')
    
    
    
    
admin.site.register(Person, PersonAdmin)
