from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Recipe


class RecipeForm(forms.ModelForm):
    """Form to create a recipe"""
    class Meta:
        model = Recipe
        fields = [
            "title",
            "description",
            "ingredients",
            "method",
            "image",
            "image_alt",
            "dish_type",
            "prep_time"
        ]
        ingredients = forms.CharField(widget=RichTextWidget())
        method = forms.CharField(widget=RichTextWidget())

        widget = {
            "description": forms.Textarea(attrs={"rows": 4}),
        }

        labels = {
            "title": "Title",
            "description": "Description",
            "ingredients": "Ingredients",
            "method": "Method",
            "image": "Image",
            "image_alt": "Describe Image",
            "dish_type": "Dish Type",
            "prep_time": "Prep Time",
        }
