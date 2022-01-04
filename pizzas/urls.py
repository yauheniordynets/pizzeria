"""URL schema for pizzas."""

from django.urls import path
from . import views

app_name = 'pizzas'
urlpatterns = [
    # Homepage
    path('', views.index, name='index'),
    # Pizzas list
    path('pizzas', views.pizzas, name='pizzas'),
    # Pizza composition
    path('toppings/<int:pizza_id>/', views.topping, name='toppings'),
    # New pizza creation
    path('new_pizza/', views.new_pizza, name='new_pizza'),
    # New topping creation
    path('new_topping/<int:pizza_id>/', views.new_topping, name='new_topping'),
    # Topping redacting page
    path('edit_topping/<int:topping_id>/', views.edit_topping, name='edit_topping')
]
