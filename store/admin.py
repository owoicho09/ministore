from django.contrib import admin
from .models import Products,ItemGallery,Items
# Register your models here.

class ItemGalleryAdmin(admin.ModelAdmin):
    list_display = ('thumbnail', 'item')

class ItemGalleryInline(admin.TabularInline):
    model = ItemGallery


class ItemAdmin(admin.ModelAdmin):
    inlines = [ItemGalleryInline]
    list_display = ('name','product', 'price')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Products)
admin.site.register(Items, ItemAdmin)
admin.site.register(ItemGallery,ItemGalleryAdmin)