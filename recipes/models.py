from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

from recipes.managers import PublishedManager

CustomUser = get_user_model()


class Ingredient(models.Model):
    """Ингредиент"""
    name = models.CharField(max_length=250, verbose_name='Наименование', null=False, blank=False)
    description = models.CharField(max_length=500, verbose_name='Описание', null=True, blank=True)
    unit = models.CharField(max_length=45, verbose_name='Единица измерения')

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

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
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

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
    status = models.CharField(verbose_name='Статус рецепта',
                              max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')
    slug = models.SlugField(max_length=250,
                            verbose_name='slug',
                            unique_for_date='created_at')

    # Default manager
    objects = models.Manager()
    # Опубликованные рецепты
    published_recipes = PublishedManager()

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def get_absolute_url(self):
        return reverse('recipe_details',
                       args=[self.created_at.strftime('%Y'),
                             self.created_at.strftime('%m'),
                             self.created_at.strftime('%d'),
                             self.slug,
                             ])

    def __str__(self):
        return f'{self.title}: {self.cooking_steps[:40]}'


class RecipeIngredients(models.Model):
    """ManyToMany с количеством каждого ингредиента по рецепту"""
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='recipe_ingredients')
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(verbose_name='Количество')
