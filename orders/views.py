from django.shortcuts import render, redirect
from .forms import PizzaForm, SubForm, PastaForm, SaladForm, DinnerPlatterForm
from .models import Pizza
from cart.views import get_cart_items
from django.http import JsonResponse


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


def get_price(request):
    style = request.GET.get('style')
    size = request.GET.get('size')
    num_toppings = request.GET.get('num_toppings')
    is_special = request.GET.get('is_special')
    if is_special == 'true':
        is_special = True
    else:
        is_special = False

    if is_special:
        # numtoppings doesn't matter
        menu_pizza = Pizza.objects.get(style=style, size=size, is_special=is_special)
    else:
        menu_pizza = Pizza.objects.get(style=style, size=size, num_toppings=num_toppings, is_special=is_special)
    price = menu_pizza.price

    print(price)
    data = {
        'price': price
    }
    return JsonResponse(data)
