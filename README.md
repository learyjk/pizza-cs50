# Project 3

This is Project 3 - Pinochio's Pizza for CS50 Web.

Requirements for the project:
https://docs.cs50.net/web/2020/x/projects/3/project3.html

Live link (please excuse slow speeds but the hosting is free!):
https://pizza-project3-cs50.herokuapp.com

Pinochio's Pizza Menu:
https://www.pinocchiospizza.net/menu.html

This website allows users to order items form Harvard's famous Pinochio's Pizza Restaurant.  Users must first register and login after which they will have access to the full menu by clicking the title "Pinochio's Pizza" in the top left.  This website was designed using Django with sqlite (local) and Postgres (Heroku) and is my first time using jQuery.  Users are handled by Djangos integrated authentication system, and allows staff users to update the menu and to manage customer orders.  Customers can login to browse the menu and place orders.

The main page to order pulls menu items from the database and provides live price updates as the user changes selection using jQuery and AJAX.  Once a user presses the "Add to Cart" button, their order will go to the cart where they can then opt to add more or checkout.  After checking out, their CartItem becomes an OrderItem and is assigned a status (pending/complete) and a date/time.  A staff user can go to the 'orders' page or the Django 'admin' page to mark orders as complete.

I chose to implement the "special" pizza option to mean Gluten Free Crust.

My personal touch is the functionality to mark orders as complete and also the live price updates.  After completing a majority of the project, I realized that the user had no price information as they selected their food.  I think that most people order food with the price in mind and was looking for an excuse to learn AJAX.


Bugs/Issues:
1. jQuery Code to catch edge case of Sausage, Peppers, Onion Sub only in allowed in Large size works first time but you can change the select menu to 'Small' after that and try to pull for a menu item that doesn't exist that way.  Gives DoesNotExist error.  Consider performing the data validation on submit rather than on change.
2. Cannot add DinnerPlatter items to cart.

Notes:
1. I started this project wildly confused with Django.  The following Udemy course helped me incredibly to understand Django basics and I would highly recommend if you are having difficulties getting started:
https://www.udemy.com/course/python-django-dev-to-deployment/learn/lecture/12056452#overview
