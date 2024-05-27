from django.urls import path

from . import views

urlpatterns = [
    path("homepage", views.homepage, name="homepage"),
    path("order_new", views.order_new, name="order_new"),
    path("ticket_list/tickets", views.ticket_list, name="ticket_list"),
    path("order_list/orders", views.order_list, name="order_list"),
    path("order/<int:order_id>/", views.order_detail, name="order_detail"),
]
