from django.urls import path

from . import views

urlpatterns = [
    path("", views.cart, name="cart"),
    path("remove/<int:cart_item_id>/", views.remove, name="remove"),
    path("checkout", views.checkout, name="checkout"),
    path("mark_complete/<int:order_item_id>/", views.mark_complete, name="mark_complete")
]
