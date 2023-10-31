from django.contrib.auth import get_user_model
from django.db import models

from recipes.managers import PublishedManager

CustomUser = get_user_model()


class Ingredient(models.Model):
    """Ингридиент"""
    name = models.CharField(max_length=250, verbose_name='Наименование', null=False, blank=False)
    description = models.CharField(max_length=500, verbose_name='Описание', null=True, blank=True)
    unit = models.CharField(max_length=45, verbose_name='Единица измерения')

    class Meta:
        verbose_name = 'Ингридиент'
        verbose_name_plural = 'Ингридиенты'

    def __str__(self):
        return self.name


class Category(models.Model):
    """Категория рецепта"""
    category = models.CharField(max_length=100, verbose_name='Категория', null=False, blank=False)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.category


class Recipe(models.Model):
    """Рецепт"""
    author = models.ForeignKey(CustomUser,
                               verbose_name='Автор',
                               related_name='recipes',
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name='Название', null=False, blank=False)
    description = models.CharField(max_length=250, verbose_name='Описание', null=False, blank=False)
    # TODO: image upload
    recipe_image = models.ImageField(upload_to='users/%Y/%m/%d/')
    cooking_steps = models.TextField(verbose_name='Шаги приготовления', null=False, blank=False)
    cooking_time = models.DurationField(verbose_name='Время приготовления, мин')
    category = models.ForeignKey(Category,
                                 verbose_name='Категория рецепта',
                                 on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(Ingredient,
                                         verbose_name='Ингредиенты',
                                         through='RecipeIngredients')
    created_at = models.DateTimeField(verbose_name='Дата создания',
                                      auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата последнего обновления',
                                      auto_now=True)
    published = models.BooleanField(verbose_name='Опубликован', default=True)

    # Default manager
    objects = models.Manager()
    # Опубликованные рецепты
    published_recipes = PublishedManager()

    class Meta:
        ordering = ('created_at',)
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return f'{self.title}: {self.cooking_steps[:40]}'


class RecipeIngredients(models.Model):
    """ManyToMany с количеством каждого ингредиента по рецепту"""
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(verbose_name='Количество')
