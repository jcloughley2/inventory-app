from django.contrib import admin

# import your model
from collection.models import List

# set up automated slug creation
class ListAdmin(admin.ModelAdmin):
    model = List
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}

# and register it
admin.site.register(List, ListAdmin)