from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('', views.recipes_list, name='recipes_list'),
    # post views
    path('<int:year>/<int:month>/<int:day>/<slug:recipe>/',
         views.recipe_details,
         name='recipe_details'),
]
