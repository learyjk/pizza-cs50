from django.urls import path

from . import views

urlpatterns = [
    path("", views.cart, name="cart"),
    path("remove/<int:cart_item_id>/", views.remove, name="remove")
]
