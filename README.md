# Проект “Сайт рецептов” на Django
## Подробное описание задания 
Создайте проект Django и приложение(я) для сайта рецептов. 
### Модели 
Для работы с пользователями используйте встроенного в Django User`a.   
Подготовьте нижеперечисленные модели: 
- Рецепты
  - Название 
  - Описание 
  - Шаги приготовления 
  - Время приготовления 
  - Изображение 
  - Автор 
  - *другие поля на ваш выбор, например ингредиенты и т.п. 
- Категории рецептов 
  - Название 
  - *другие поля на ваш выбор 
- Связующая таблица для связи Рецептов и Категории
  - обязательные для связи поля
  - *другие поля на ваш выбор 
### Шаблоны 
Подготовьте базовый шаблон проекта и нижеперечисленные дочерние шаблоны: 
- Главная с 5 случайными рецептами кратко
- Страница с одним подробным рецептом
- Страницы регистрации, авторизации и выхода пользователя
- Страница добавления/редактирования рецепта
- *другие шаблоны на ваш выбор
### Формы
Создайте формы для ввода и редактирования информации (рецептов) в вашем проекте. 
Интегрируйте их в шаблоны. 
### Представления
Создайте представления, которые охватывают весь ваш проект: модели, формы, 
шаблоны. 
### Маршруты
Подключите маршруты, убедитесь в работоспособности представлений и связанных 
с ними моделей, форм и шаблонов. 
### Облачный сервер и наполнение
Разверните рабочий проект на сервере. Наполните базу данных как минимум 
пятью рецептами

## Реализация
### Создаем проект, настраиваем репозиторий
```shell
Windows PowerShell
(C) Корпорация Майкрософт (Microsoft Corporation). Все права защищены.

Установите последнюю версию PowerShell для новых функций и улучшения! https://aka.ms/PSWindows

(venv) PS C:\Users\eugen\PycharmProjects\bookOfRecipes> git remote add origin git@github.com:blinktreeman/bookOfRecipes.git
(venv) PS C:\Users\eugen\PycharmProjects\bookOfRecipes> git push -u origin master
Enumerating objects: 16, done.
Counting objects: 100% (16/16), done.
Delta compression using up to 12 threads
Compressing objects: 100% (14/14), done.
Writing objects: 100% (16/16), 4.11 KiB | 2.06 MiB/s, done.
Total 16 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), done.
To github.com:blinktreeman/bookOfRecipes.git
 * [new branch]      master -> master
branch 'master' set up to track 'origin/master'.
(venv) PS C:\Users\eugen\PycharmProjects\bookOfRecipes> git pull
remote: Enumerating objects: 4, done.
remote: Counting objects: 100% (4/4), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (3/3), 2.14 KiB | 274.00 KiB/s, done.
From github.com:blinktreeman/bookOfRecipes
   2927ab0..d0e866e  master     -> origin/master
Updating 2927ab0..d0e866e
Fast-forward
 .gitignore | 160 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 1 file changed, 160 insertions(+)
 create mode 100644 .gitignore
(venv) PS C:\Users\eugen\PycharmProjects\bookOfRecipes> git checkout -b dev_recipes
Switched to a new branch 'dev_recipes'
(venv) PS C:\Users\eugen\PycharmProjects\bookOfRecipes>
```
### Создаем приложения "Рецепты", "Пользователи"
```shell
(venv) PS C:\Users\eugen\PycharmProjects\bookOfRecipes> python manage.py startapp recipes
(venv) PS C:\Users\eugen\PycharmProjects\bookOfRecipes> python manage.py startapp accounts
(venv) PS C:\Users\eugen\PycharmProjects\bookOfRecipes> 
```
И добавим приложения в файл конфигурации указав ссылку на классы конфигурации приложений  
[https://docs.djangoproject.com/en/4.2/ref/applications/#configuring-applications](https://docs.djangoproject.com/en/4.2/ref/applications/#configuring-applications)  
`settings.py`:
```python
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # recipes application
    'recipes.apps.RecipesConfig',
    # accounts application
    'accounts.apps.AccountsConfig',
]
```
### Модель пользователя
Для модели пользователя можно использовать встроенного в Django User`a, 
но, как рекомендует Django doc:

> [Using a custom user model when starting a project](https://docs.djangoproject.com/en/4.2/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project)  

В `accounts/models.py` зададим пользовательскую модель:
```python
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass
```
В `settings.py` переопределяем модель по умолчанию:
```python
AUTH_USER_MODEL = 'accounts.User'
```
Регистрируем модель пользователя в админке Django. В `accounts/admin.py`:
```python
from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
```
### Модели recipes
