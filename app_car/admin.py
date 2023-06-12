from django.contrib import admin
from.models import Contact,Services,Booking

# Register your models here.


@admin.register(Services)
class serviceAdmin(admin.ModelAdmin):
    list_display=('title','headline','service_img','created_at')
    




@admin.register(Contact)
class contactAdmin(admin.ModelAdmin):
    list_display=('name','email','phone_number','created_at')
    search_fields = ('name',)
    list_filter =('created_at',)
    list_per_page = 10


@admin.register(Booking)
class bookingAdmin(admin.ModelAdmin):
    list_display=('name','email','phone_number','created_at')
    search_fields = ('name',)
    list_filter =('created_at',)
    list_per_page = 10
