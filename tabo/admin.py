from django.contrib import admin
from .models import Processed,Scraped

@admin.register(Processed)
class ProcessedAdmin(admin.ModelAdmin):
    search_fields = ['time']
    list_display = ['time', 'temperature']
    readonly_fields = ["time",'temperature']
    list_per_page = 50


@admin.register(Scraped)
class ScrapedAdmin(admin.ModelAdmin):
    search_fields = ['time']
    list_display = ['time', 'temperature']
    readonly_fields = ["time",'temperature']
    list_per_page = 50
