from django.contrib import admin

# import your model
from collection.models import List, Item


class ItemAdmin(admin.TabularInline):
    model = Item
    # item_display = ('name')

# set up automated slug creation
class ListAdmin(admin.ModelAdmin):
    model = List
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}
    inlines = [
        ItemAdmin
    ]

# and register it




# admin.site.register(Item, ItemAdmin)
admin.site.register(List, ListAdmin)

