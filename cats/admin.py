from django.contrib import admin

from .models import Cat

@admin.register(Cat)
class CatAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'color',
        'birth_year'
    )