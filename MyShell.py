import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","Pizzeria.settings")
import django
django.setup()

from Pizzerias.models import Pizza

pizzas = Pizza.objects.all()
for pizza in pizzas:
    print(pizza.id, pizza)