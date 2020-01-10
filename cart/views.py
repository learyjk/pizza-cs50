from django.shortcuts import render, redirect
from orders.forms import PizzaForm, SubForm, PastaForm, SaladForm, DinnerPlatterForm
from orders.models import Pizza, Sub, Pasta, Salad, DinnerPlatter
from cart.models import CartItem
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
        elif request.POST['menu_item'] == 'Dinner Platter':
            form = DinnerPlatterForm(request.POST)
            if form.is_valid():
                form = form.cleaned_data
                menu = 'Dinner Platter'
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

        context = {
            'cart_items': cart_items,
            'num_cart_items': cart_items.count()
        }

        return render(request, 'cart/cart.html', context)

    else:

        # Display Shopping Cart for GET request
        cart_items = get_cart_items(request)

        context = {
            'cart_items': cart_items,
            'num_cart_items': cart_items.count()
        }
        return render(request, 'cart/cart.html', context)


# Helper Funcitons
def get_cart_items(request):
    cart_items = CartItem.objects.filter(user_id=request.user.id)
    return cart_items
