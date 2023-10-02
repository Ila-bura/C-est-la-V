from django.contrib import admin
from .models import Recipe


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "dish_type",
        "prep_time",
        "method",
        "ingredients",
        "image",
    )
    list_filter = ("dish_type",)
