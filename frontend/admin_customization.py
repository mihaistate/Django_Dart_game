from django.contrib import admin
from myapp.models import HelpRequest

class HelpRequestAdmin(admin.ModelAdmin):
    search_fields = ['staff_id', 'pokemon__name', 'user__email']

admin.site.register(HelpRequest, HelpRequestAdmin)