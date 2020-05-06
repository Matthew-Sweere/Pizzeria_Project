from django.shortcuts import render, redirect
from .forms import PizzaForm, ToppingForm
from .models import Pizza, Topping

# Create your views here.

# When a URL requests matches the pattern we just defined,
# Django looks for a function called index() in the views.py file

def index(request):
    """The home page for Pizzeria."""
    return render(request, 'Pizzerias/index.html')

    
def pizzas(request):
    # A context is a dictionary in which the keys are names we'll use
    # in the template to access the data, and the values are the data
    # we need to send to the template. In this case, there is one key-value pair,
    # which contains the set of topics we'll display on the page.
    context = {'pizzas':pizzas}
    # When building a page that uses data, we pass the context variable to render()
    # as well as the request object and the path to the template
    return render(request, 'Pizzerias/pizzas.html', context)

def pizza(request, pizza_id):
    # just like we did in MyShell.py
    pizza = Pizza.objects.get(id = pizza_id)
    # foreign key can be accessed using '_set'
    context = {'pizza': pizza, 'toppings': toppings}

    return render(request, 'Pizzerias/pizza.html', context)


def new_pizza(request):
    if request.method != 'POST':
        # No data submitted; create a blank form (create an instance of TopicForm).
        # Because we included no arguments when instantiating TopicForm, Django
        # creates a blank form that the user can fill out
        form = PizzaForm()
    else:
        # POST data submitted; process data
        # We make an instance of TopicForm and pass it the data entered by the user,
        # stored in request.POST
        form = PizzaForm(data = request.POST)
        # The is_valid() method checks that all required fields have been filled
        # in (all fields in a form are required by default) and that the data entered
        # matches the field types expected
        if form.is_valid():
            # write the data from the form to the database
            form.save()
            # redirect the user's browser to the topics page
            return redirect('Pizzerias:pizzas')

    # Display a blank form using the new_topic.html template
    context = {'form': form}
    return render(request, 'Pizzerias/new_pizza.html', context)

def new_topping(request, pizza_id):
    pizza = Pizza.objects.get(id = pizza_id)
    if request.method != 'POST':
        form = ToppingForm()
    else:
        form = ToppingForm(data = request.POST)

        if form.is_valid():
            # When we call save(), we include the argument commit=False to tell Django to create
            # a new entry object and assign it to new_entry without saving it to the database yet.
            new_topping = form.save(commit=False)
            # assigns the topic of the new entry based on the topic we pulled from topic_id
            new_topping.pizza = pizza
            new_topping.save()
            form.save()
            return redirect('Pizzerias:pizza', pizza_id = pizza_id)

    context = {'form': form, 'pizza': pizza}
    return render(request, 'Pizzerias/new_topping.html', context)


def edit_topping(request, topping_id):
    """Edit an existing topping."""
    topping = Topping.objects.get(id=topping_id)
    pizza = topping.pizza

    if request.method != 'POST':
        # This argument tells Django to create the form prefilled
        # with information from the existing entry object
        form = ToppingForm(instance = topping)
    else:
        # POST data submitted; process data
        form = ToppingForm(instance = topping, data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('Pizzerias:pizza', pizza_id = pizza.id)

    context = {'topping': topping, 'pizza': pizza, 'form': form}
    return render(request, 'Pizzerias/edit_topping.html', context)

