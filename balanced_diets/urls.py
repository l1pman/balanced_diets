from django.urls import path

from . import views
app_name = 'balanced_diets'
urlpatterns = [
    path('', views.index, name='index'),
    path('new_kcal/', views.new_kcal, name='new_kcal'),
    path('my_diet/', views.my_diet, name='my_diet'),
    path('edit_kcal/', views.edit_kcal, name='edit_kcal')
]