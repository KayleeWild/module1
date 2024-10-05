from django.contrib import admin
from items.models import Item, Cart

# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    pass

admin.site.register(Item, ItemAdmin)

class CartAdmin(admin.ModelAdmin):
    pass

admin.site.register(Cart, CartAdmin)