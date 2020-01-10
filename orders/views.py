from django.shortcuts import render, redirect
from .forms import PizzaForm, SubForm, PastaForm, SaladForm, DinnerPlatterForm
from cart.models import CartItem
from cart.views import get_cart_items


def index(request):

    if request.user.is_authenticated:

        data = {
            'Pizza': PizzaForm(),
            'Sub': SubForm(),
            'Pasta': PastaForm(),
            'Salad': SaladForm(),
            'Dinner Platter': DinnerPlatterForm()
            }

        cart_items = get_cart_items(request)

        context = {
            'data': data,
            'num_cart_items': cart_items.count()

        }
        return render(request, 'orders/index.html', context)
    else:
        return redirect('login')
