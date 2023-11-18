from django import forms

from .models import Category, Ingredient, Recipe


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
       