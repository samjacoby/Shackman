from btype.models import Typeface, Variant
from django.contrib import admin

class VariantInline(admin.StackedInline):
    model = Variant
    extra = 1

class TypefaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'designer')
    list_filter = ['name']
    inlines = [VariantInline]

admin.site.register(Typeface, TypefaceAdmin)
