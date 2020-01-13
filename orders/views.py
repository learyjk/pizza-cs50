from django.shortcuts import render, redirect
from .forms import PizzaForm, SubForm, PastaForm, SaladForm, DinnerPlatterForm
from .models import Pizza, Sub, Pasta, Salad, DinnerPlatter
from cart.views import get_cart_items
from django.http import JsonResponse
from decimal import Decimal


def index(request):

    if request.user.is_authenticated:

        data = {
            'Pizza': PizzaForm(),
            'Sub': SubForm(),
            'Pasta': PastaForm(),
            'Salad': SaladForm(),
            'DinnerPlatter': DinnerPlatterForm()
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
    menu_item = request.GET.get('menu_item')
    price = "--.--"
    if menu_item == 'Pizza':
        style = request.GET.get('style')
        size = request.GET.get('size')
        num_toppings = request.GET.get('num_toppings')
        is_special = request.GET.get('is_special')
        if is_special == 'true':
            is_special = True
        else:
            is_special = False

        if style != "" and size != "" and num_toppings != "":
            if is_special:
                # numtoppings doesn't matter
                menu_pizza = Pizza.objects.get(style=style, size=size, is_special=is_special)
            else:
                menu_pizza = Pizza.objects.get(style=style, size=size, num_toppings=num_toppings, is_special=is_special)
            price = menu_pizza.price
    elif menu_item == 'Sub':
        ingredients = request.GET.get('ingredients')
        size = request.GET.get('size')
        extras = request.GET.get('extras')
        if ingredients != "" and size != "":
            menu_sub = Sub.objects.get(ingredients=ingredients, size=size)
            price = menu_sub.price + Decimal(0.50)*int(extras)
    elif menu_item == 'Pasta':
        style = request.GET.get('style')
        menu_pasta = Pasta.objects.get(style=style)
        price = menu_pasta.price
    elif menu_item == 'Salad':
        style = request.GET.get('style')
        menu_salad = Salad.objects.get(style=style)
        price = menu_salad.price
    elif menu_item == 'DinnerPlatter':
        style = request.GET.get('style')
        size = request.GET.get('size')
        if style != "" and size != "":
            menu_dinner_platter = DinnerPlatter.objects.get(style=style, size=size)
            price = menu_dinner_platter.price
    else:
        price = "--.--"
    data = {
        'price': price
    }
    return JsonResponse(data)
