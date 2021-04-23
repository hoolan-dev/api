from django.contrib import admin

from property.models import Property


@admin.action(description='Generate Solana id')
def generate_solana_id_admin(modeladmin, request, queryset):
    for property in queryset:
        print(property.id)


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('catastro_id', 'solana_id', 'date_created',)
    search_fields = ('catastro_id', 'solana_id', 'id',)
    actions = (generate_solana_id_admin,)
