import random

from django.shortcuts import render, get_object_or_404

from .models import Recipe


# https://docs.djangoproject.com/en/4.2/intro/tutorial03/#a-shortcut-render
def home(request):
    recipes = list(Recipe.published_recipes.all())
    recipes = random.sample(recipes, 5)
    return render(request,
                  'home.html',
                  {'recipes': recipes})


def recipes_list(request):
    recipes = Recipe.published_recipes.all()
    return render(request,
                  'recipes-list.html',
                  {'recipes': recipes})


def recipe_details(request, year, month, day, recipe):
    recipe = get_object_or_404(Recipe,
                               slug=recipe,
                               status='published',
                               created_at__year=year,
                               created_at__month=month,
                               created_at__day=day)
    #ingredients = recipe.ingredients.all()
    return render(request,
                  'recipe-details.html',
                  {'recipe': recipe,})
                   #'ingredients': ingredients})
