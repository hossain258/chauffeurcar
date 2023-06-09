from django.contrib import admin
from.models import Contact

# Register your models here.



@admin.register(Contact)
class contactAdmin(admin.ModelAdmin):
    list_display=('name','email','phone_number','date_created')
    search_fields = ('name',)
    list_filter =('date_created',)
    list_per_page = 10
