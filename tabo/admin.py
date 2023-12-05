from django.contrib import admin
from .models import Processed,Scraped

@admin.register(Processed)
class StockAdmin(admin.ModelAdmin):
    search_fields = ['time']
    list_display = ['time', 'temperature']
    readonly_fields = ["time",'temperature']


@admin.register(Scraped)
class StockAdmin(admin.ModelAdmin):
    search_fields = ['time']
    list_display = ['time', 'temperature']
    readonly_fields = ["time",'temperature']