from django.contrib import admin

# Register your models here.

from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published',
                    'price', 'list_data', 'realtor')
    list_display_links = ('title',)
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'address',
                     'city', 'location', 'zipcode', 'price')
    list_per_page = 25


admin.site.register(Listing, ListingAdmin)
