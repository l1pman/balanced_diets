from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Dish(models.Model):
    meals = [
        ('B', 'Завтрак'),
        ('L', 'Обед'),
        ('D', 'Ужин')
    ]
    name = models.CharField(max_length=50)
    kcal = models.DecimalField(max_digits=6, decimal_places=2)
    proteins = models.DecimalField(max_digits=6, decimal_places=2)
    fats = models.DecimalField(max_digits=6, decimal_places=2)
    carbs = models.DecimalField(max_digits=6, decimal_places=2)
    meal = models.CharField(max_length=15, choices=meals, default='')
    lactose = models.BooleanField()
    vegan = models.BooleanField()
    diabetes = models.BooleanField()

class Product(models.Model):
    name = models.CharField(max_length=50)

class Recipe(models.Model):
    id_dish = models.ForeignKey(Dish, on_delete=models.DO_NOTHING)
    id_product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)

class New_kcal(models.Model):
    genders = [
        ('M', 'Мужской'),
        ('F', 'Женский')
    ]
    activities = [
        ('1,2', 'Сидячий образ жизни.'),
        ('1,375', 'До трех малоинтенсивных тренировок в неделю.'),
        ('1,55', 'Тренировки три-четыре раза в неделю, тренировки интенсивные, но не тяжелые.'),
        ('1,7', 'Ежедневные занятия спортом или ежедневная работа, связанная с большим количеством перемещений и ручного труда.'),
        ('1,9', 'Экстремальная активность. Профессиональный спортсмен или работа с тяжестями и т.д.')
    ]
    name = models.CharField(max_length=150)
    gender = models.CharField(max_length=10, choices=genders, default='')
    weight = models.IntegerField()
    height = models.IntegerField()
    age = models.IntegerField()
    activity = models.CharField(max_length=50, choices=activities, default='')
    lactose = models.BooleanField(default=False)
    vegan = models.BooleanField(default=False)
    diabetes = models.BooleanField(default=False)


class exclusion_product(models.Model):
    id_user = models.ForeignKey(New_kcal, on_delete=models.DO_NOTHING)
    id_product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
