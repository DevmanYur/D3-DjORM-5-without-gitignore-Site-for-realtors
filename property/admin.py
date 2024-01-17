from django.contrib import admin

from .models import Flat, Claim, Owner


class Owned_flats_Inline(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ('owner','flat',)

@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owner']
    readonly_fields = ['created_at']
    list_display = ['id','address', 'price', 'new_building', 'town', 'construction_year']
    list_editable = ['new_building']
    list_filter = ['new_building', 'rooms_number', 'has_balcony']
    raw_id_fields = ('liked_by',)
    inlines = [Owned_flats_Inline,]

@admin.register(Claim)
class ClaimAdmin(admin.ModelAdmin):
    raw_id_fields = ('author','flat',)
    list_display = ['author', 'flat']
    search_fields = ['author']

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flats',)
    list_display = ['id', 'fullname', 'pure_phone']
    search_fields = ['fullname']
    inlines = [Owned_flats_Inline, ]