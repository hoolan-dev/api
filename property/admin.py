from django.contrib import admin

from property.models import Property


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('catastro_id', 'solana_id', 'date_created',)
    search_fields = ('catastro_id', 'solana_id', 'id',)
