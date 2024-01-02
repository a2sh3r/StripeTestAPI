from django.contrib import admin
from django.contrib.admin import ModelAdmin

from items.models import Item


@admin.register(Item)
class ItemAdmin(ModelAdmin):
    list_display = (
        "id",
        "name",
        "price",
    )
