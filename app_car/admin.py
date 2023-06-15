from django.contrib import admin
from.models import Contact,Services,Booking,Review
from django.templatetags.static import static

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
    list_display=('name','email','phone_number','status','created_at',)
    actions = ['mark_action_pending']
    search_fields = ('name',)
    list_filter =('created_at','status')
    list_per_page = 10

    class Media:
        css = {
            'all': (static('css/admin.css'),)
        }

    def mark_action_pending(modeladmin, request, queryset):
        queryset.update(status='action_pending')
        modeladmin.message_user(request, "Selected bookings have been marked as Action Pending.")

    mark_action_pending.short_description = "Mark selected bookings as Action Pending"

@admin.register(Review)
class reviewAdmin(admin.ModelAdmin):
    list_display=('name','email','status','is_published','created_at',)
    actions = ['mark_action_pending']
    search_fields = ('name',)
    list_filter =('created_at','status')
    list_per_page = 10

