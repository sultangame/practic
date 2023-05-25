from django.contrib import admin
from .models import Team

@admin.register(Team)
class PostAdmin(admin.ModelAdmin):
    
    list_display = ['id', 'name']
    ordering = ['-id']
    search_fields = ['name']
