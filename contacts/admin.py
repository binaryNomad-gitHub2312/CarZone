from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    def inquiry_no(self, object):
        return object.id
    inquiry_no.short_description = 'Inquiry No.'
    list_display = ('inquiry_no', 'first_name', 'last_name', 'email', 'car_title', 'city', 'create_date')
    list_display_links = ('inquiry_no', 'first_name', 'last_name')
    search_fields = ('first_name', 'last_name', 'email', 'car_title')
    list_per_page = 25

# Register your models here.
admin.site.register(Contact, ContactAdmin)