import os
import subprocess

from django.contrib import admin

from property.models import Property, Contributor


@admin.action(description='Generate Solana id')
def generate_solana_id_admin(modeladmin, request, queryset):
    for property_obj in queryset:
        # output = os.system("spl-token create-token")
        create_token = subprocess.getstatusoutput(f'spl-token create-token')
        token_id = create_token[1].split(" ")[2].split("\n")[0]
        create_account = subprocess.getstatusoutput(f'spl-token create-account {token_id}')
        account_id = create_account[1].split("\n")[0].split(" ")[2]
        mint_token = subprocess.getstatusoutput(f'spl-token mint {token_id} 1 {account_id}')
        disable_mint_token = subprocess.getstatusoutput(f'spl-token authorize {token_id} mint --disable')
        property_obj.solana_id = token_id
        property_obj.save()
        print(property_obj.id)


@admin.action(description='Generate Solana id')
def generate_solana_id_admin(modeladmin, request, queryset):
    for property_obj in queryset:
        # output = os.system("spl-token create-token")
        create_token = subprocess.getstatusoutput(f'spl-token create-token')
        token_id = create_token[1].split(" ")[2].split("\n")[0]
        create_account = subprocess.getstatusoutput(f'spl-token create-account {token_id}')
        account_id = create_account[1].split("\n")[0].split(" ")[2]
        mint_token = subprocess.getstatusoutput(f'spl-token mint {token_id} 1 {account_id}')
        disable_mint_token = subprocess.getstatusoutput(f'spl-token authorize {token_id} mint --disable')
        property_obj.solana_id = token_id
        property_obj.save()
        print(property_obj.id)


@admin.register(Contributor)
class ContributorAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'identification', 'name', 'property', 'city',)


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('catastro_id', 'solana_id', 'date_created',)
    search_fields = ('catastro_id', 'solana_id', 'id',)
    actions = (generate_solana_id_admin,)
