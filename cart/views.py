from django.shortcuts import render, redirect
from orders.forms import PizzaForm, SubForm, PastaForm, SaladForm, DinnerPlatterForm
from orders.models import Pizza, Sub, Pasta, Salad, DinnerPlatter
from cart.models import CartItem, OrderItem
from django.db.models import Sum
from decimal import Decimal


# Create your views here.
def cart(request):
    if request.method == "POST":
        if request.POST['menu_item'] == 'Pizza':
            form = PizzaForm(request.POST)

            if form.is_valid():
                form = form.cleaned_data
                # Get the form data to build a Pizza and CartItem
                menu = "Pizza"
                style = form['style']
                size = form['size']
                is_special = False
                if 'is_special' in request.POST:
                    is_special = True
                num_toppings = form['num_toppings']
                topping_list = []
                for topping in form['toppings']:
                    topping_list.append(str(topping))
                toppings = ", ".join(topping_list)

                # Lookup price
                if is_special:
                    # numtoppings doesn't matter
                    menu_pizza = Pizza.objects.get(style=style, size=size, is_special=is_special)
                else:
                    menu_pizza = Pizza.objects.get(style=style, size=size, num_toppings=num_toppings, is_special=is_special)
                price = menu_pizza.price
                print(price)

                # Create the Cart Item
                order = CartItem(menu=menu, size=size, style=style, additional=toppings, is_special=is_special, user_id=request.user.id, price=price)
                order.save()

        elif request.POST['menu_item'] == 'Sub':
            form = SubForm(request.POST)
            if form.is_valid():
                form = form.cleaned_data
                menu = 'Sub'
                ingredients = form['ingredients']
                size = form['size']
                extras_list = []
                added_cost = Decimal(0.00)
                for extra in form['extras']:
                    extras_list.append(str(extra))
                    added_cost += extra.added_cost

                extras = ", ".join(extras_list)

                # Lookup price
                menu_sub = Sub.objects.get(ingredients=ingredients, size=size)
                price = menu_sub.price + Decimal(added_cost)

                # Create the Cart Item
                order = CartItem(menu=menu, size=size, style=ingredients, additional=extras, is_special=False, user_id=request.user.id, price=price)
                order.save()

            redirect('index')
        elif request.POST['menu_item'] == 'Pasta':
            form = PastaForm(request.POST)
            if form.is_valid():
                form = form.cleaned_data
                menu = 'Pasta'
                style = form['style']

                # Lookup price
                menu_pasta = Pasta.objects.get(style=style)
                price = menu_pasta.price

                # Create the Cart Item
                order = CartItem(menu=menu, style=style, user_id=request.user.id, price=price)
                order.save()
        elif request.POST['menu_item'] == 'Salad':
            form = SaladForm(request.POST)
            if form.is_valid():
                form = form.cleaned_data
                menu = 'Salad'
                style = form['style']

                # Lookup price
                menu_salad = Salad.objects.get(style=style)
                price = menu_salad.price

                # Create the Cart Item
                order = CartItem(menu=menu, style=style, user_id=request.user.id, price=price)
                order.save()
        elif request.POST['menu_item'] == 'DinnerPlatter':
            form = DinnerPlatterForm(request.POST)
            if form.is_valid():
                form = form.cleaned_data
                menu = 'DinnerPlatter'
                style = form['style']
                size = form['size']

                # Lookup price
                menu_dinner_platter = DinnerPlatter.objects.get(style=style, size=size)
                price = menu_dinner_platter.price

                # Create the Cart Item
                order = CartItem(menu=menu, style=style, size=size, user_id=request.user.id, price=price)
                order.save()
        else:
            print("Post Error")
            redirect('index')

        cart_items = get_cart_items(request)
        if cart_items:
            total_cost = Decimal(cart_items.aggregate(Sum('price'))['price__sum'])
        else:
            total_cost = 0

        context = {
            'cart_items': cart_items,
            'num_cart_items': cart_items.count(),
            'total_cost': total_cost
        }

        return render(request, 'cart/cart.html', context)

    else:

        # Display Shopping Cart for GET request
        cart_items = get_cart_items(request)
        if cart_items:
            total_cost = Decimal(cart_items.aggregate(Sum('price'))['price__sum'])
        else:
            total_cost = 0

        context = {
            'cart_items': cart_items,
            'num_cart_items': cart_items.count(),
            'total_cost': total_cost
        }
        return render(request, 'cart/cart.html', context)


def checkout(request):
    if request.method == "POST":

        cart_items = get_cart_items(request)

        for item in cart_items:
            menu = item.menu
            size = item.size
            style = item.style
            additional = item.additional
            is_special = item.is_special
            price = item.price
            user_id = item.user_id
            order = OrderItem(menu=menu, size=size, style=style, additional=additional, is_special=is_special, price=price, user_id=user_id)
            order.save()
            item.delete()

        all_order_items = OrderItem.objects.order_by('is_complete', 'created_at')

        user_order_items = all_order_items.filter(user_id=request.user.id)
        cart_items = get_cart_items(request)

        context = {
            'cart_items': cart_items,
            'all_order_items': all_order_items,
            'user_order_items': user_order_items,
            'num_cart_items': cart_items.count(),
        }

        return render(request, 'cart/checkout.html', context)
    else:
        all_order_items = OrderItem.objects.order_by('is_complete', 'created_at')

        user_order_items = all_order_items.filter(user_id=request.user.id)
        cart_items = get_cart_items(request)

        context = {
            'cart_items': cart_items,
            'all_order_items': all_order_items,
            'user_order_items': user_order_items,
            'num_cart_items': cart_items.count(),
        }

        return render(request, 'cart/checkout.html', context)


def remove(request, cart_item_id):
    cart_item = CartItem.objects.filter(id=cart_item_id)
    cart_item.delete()
    return redirect('cart')


def mark_complete(request, order_item_id):
    order_item = OrderItem.objects.filter(id=order_item_id)
    order_item.update(is_complete=True)
    return redirect('checkout')


# Helper Funcitons
def get_cart_items(request):
    cart_items = CartItem.objects.filter(user_id=request.user.id)
    return cart_items
