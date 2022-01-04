from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def logged_out(request):
    """Pizzas homepage"""
    return render(request, 'users/logged_out.html')


def register(request):
    """"New user registration"""
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # Log in system
            login(request, new_user)
            return redirect('pizzas:pizzas')

    context = {'form': form}
    return render(request, 'users/register.html', context)
