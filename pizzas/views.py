from django.shortcuts import render, redirect
from .models import Pizza, Topping
from .forms import PizzaForm, ToppingForm
from django.contrib.auth.decorators import login_required
from django.http import Http404


def index(request):
    """Pizzas homepage"""
    return render(request, 'pizzas/index.html')


@login_required()
def pizzas(request):
    """"Return list of pizza"""
    pizza = Pizza.objects.filter(owner=request.user)
    context = {'pizzas': pizza}
    return render(request, 'pizzas/pizzas.html', context)


@login_required()
def topping(request, pizza_id):
    """Return pizza composition"""
    pizza = Pizza.objects.get(id=pizza_id)
    if pizza.owner != request.user:
        raise Http404
    toppings = pizza.toppings.all()
    context = {'pizza': pizza, 'toppings': toppings}
    return render(request, 'pizzas/toppings.html', context)


@login_required()
def new_pizza(request):
    """Define new pizza"""
    try:
        if request.method != 'POST':
            # Data is not sent, create new form
            form = PizzaForm()
        else:
            # Data sent
            form = PizzaForm(data=request.POST)
            if form.is_valid():
                new_pizza = form.save(commit=False)
                new_pizza.owner = request.user
                new_pizza.save()
                return redirect('pizzas:pizzas')
        # Return empty form
        context = {'form': form}
        return render(request, 'pizzas/new_pizza.html', context)
    except Exception as e:
        print(e)


@login_required()
def new_topping(request, pizza_id):
    """Add new topping for pizza"""
    pizza = Pizza.objects.get(id=pizza_id)
    check_owner(request, pizza)
    if request.method != 'POST':
        # Data is not sent, create new form
        form = ToppingForm()
    else:
        # Data sent
        form = ToppingForm(data=request.POST)
        if form.is_valid():
            new_topping = form.save(commit=False)
            new_topping.pizza_name = pizza
            new_topping.save()
            return redirect('pizzas:toppings', pizza_id=pizza_id)
    # Return empty form
    context = {'pizza': pizza, 'form': form}
    return render(request, 'pizzas/new_topping.html', context)


@login_required()
def edit_topping(request, topping_id):
    """Change topping"""
    topping = Topping.objects.get(id=topping_id)
    pizza = topping.pizza_name
    check_owner(request, pizza)
    if request.method != 'POST':
        form = ToppingForm(instance=topping)
    else:
        form = ToppingForm(instance=topping, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('pizzas:toppings', pizza_id=pizza.id)
    context = {'topping': topping, 'pizza': pizza, 'form': form}
    return render(request, 'pizzas/edit_topping.html', context)


def check_owner(request, pizza):
    if pizza.owner != request.user:
        raise Http404
    return topping, pizza
