from django.contrib import admin

from .models import Ingredient, Category, Recipe, RecipeIngredients


class IngredientInLine(admin.StackedInline):
    model = RecipeIngredients
    extra = 0


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    model = Recipe

    list_display = (
        'author',
        'title',
        'description',
        'recipe_image',
        'cooking_steps',
        'cooking_time',
        'created_at',
        'updated_at',
        'status',
        'slug',
    )
    list_filter = (
        'status',
    )
    search_fields = (
        'title',
        'author',
        'created_at',
    )
    prepopulated_fields = {
        'slug': (
            'title',
        )
    }
    inlines = [
        IngredientInLine
    ]
    date_hierarchy = 'created_at'
    save_on_top = True


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient
    list_display = (
        'name',
        'description',
        'unit',
    )
    search_fields = (
        'name',
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = (
        'category',
    )
    search_fields = (
        'category',
    )
