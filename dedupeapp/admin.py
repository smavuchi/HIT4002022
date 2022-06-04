from django.contrib import admin
from .models import Deduped

# Register your models here.
# admin.site.register(Deduped)

@admin.register(Deduped)
class DedupedAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'deduped_file')
