from django.urls import path
from . import views

app_name = 'jizdenky'


urlpatterns = [
    path("homepage", views.homepage, name="homepage"),
    path("order_new", views.order_new, name="order_new"),
    path("ticket_list", views.ticket_list, name="ticket_list"),
    path("order_list", views.order_list, name="order_list"),
    path("order_detail/<str:id>/", views.order_detail, name="order_detail"),
    path("order_end", views.order_end, name="order_end"),
]
