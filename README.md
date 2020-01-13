# Project 3

This is my implementation of Project 3 - Pinochio's Pizza for CS50 Web.

Requirements for the project:
https://docs.cs50.net/web/2020/x/projects/3/project3.html

I chose "Special" as a boolean to indicate "gluten-free crust" or not.  In the model, num_toppings for special is indicated as 4, but really is just a filler value.  num_toppings could be anything for a special pizza.

My personal touch is the Orders page where a user can go track the status of his/her order ("Pending" or "Complete").  Also, a staff user will see all user orders and can mark orders as complete from this page.

Bugs/Issues:
1. No validation for Number of Toppings when user makes selections.  We trust the user to select the 'correct' number of toppings and also to not exceed 3 toppings (the max).  Some form validation would fix this.
2. Would be great to have price data available while the user builds his/her order in the forms.  Could be accomplished using AJAX requests to the Django models to get price data perhaps?
3. No max setting for checkout.  I.e. as time goes on, orders are never deleted from OrderItems table.  Since this website will never go in to production, I just decided to handle table size manually (i.e. "I'll just delete them myself when the list seems too long.").  Consider a code block that deletes completed orders after it is more than 7 days old or something like that.
4. the app names "orders" should probably be name "menu".  However, since the project template comes with the "orders" app already created, and the Requirements document says to use models.py in that app, I kept it as is.  The orders functionality is handled in the cart app by 'checkout' view.
5. jQuery Code to catch edge case of Sausage, Peppers, Onion Sub only in allowed in Large size works first time but you can change the select menu to 'Small' after that and try to pull for a menu item that doesn't exist that way.  Gives DoesNotExist error.

Notes:
1. I started this project wildly confused with Django.  The following Udemy course helped me incredibly to understand Django basics and I would highly recommend if you are having difficulties getting started:
https://www.udemy.com/course/python-django-dev-to-deployment/learn/lecture/12056452#overview
