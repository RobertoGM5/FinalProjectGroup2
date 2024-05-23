from django.contrib import admin
from .models import SupportRequest

class SupportAdmin(admin.ModelAdmin):
    list_display = ('email', 'subject', 'created_at')
    search_fields = ('email', 'subject', 'message')

admin.site.register(SupportRequest, SupportAdmin)
