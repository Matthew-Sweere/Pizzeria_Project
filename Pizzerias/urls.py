# the path function, which is needed when mapping URLs to views
from django.urls import path

# the dot tells Python to import the views.py module from
# the same directory as the current urls.py module
from . import views

# the variable app_name helps Django distinguish this urls.py file from
# files of the same name in other apps within the project
app_name = 'Pizzerias'

# The variable urlpatterns in this module is a list of individual pages
# that can be requested from the learning_logs app
urlpatterns = [
    # the first argument is an empty string (' ') which matches the
    # base URL - http://localhost:8000/. The second argument specifies 
    # the function name to call in views.py. The third argument provides
    # the name 'index' for this URL pattern to refer to it later
    path('', views.index, name = 'index'),
    path('pizzas', views.pizzas, name = 'pizzas'),
    # the integer value is stored in the variable topic_id and will
    # be subsequently passed to the topic function in views.py
    path('pizzas/<int:pizza_id>/', views.pizza, name = 'pizza'),
    path('new_pizza/', views.new_pizza, name = 'new_pizza'),
    path('new_topping/<int:pizza_id>/', views.new_topping, name = 'new_topping'),
    path('edit_topping/<int:topping_id>/', views.edit_topping, name = 'edit_topping')

]