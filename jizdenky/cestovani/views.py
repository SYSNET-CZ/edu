from django.shortcuts import render, redirect, get_object_or_404
from .forms import OrderModelForm
from .forms import TicketModelForm
from .models import Ticket, Order


def homepage(request):
    tickets = Ticket.objects.all()
    return render(request, template_name="cestovani/homepage.html", context={"tickets": tickets})


# Create your views here.

def order_new(request):
    if request.method == "POST":
        form = OrderModelForm(request.POST)
        if form.is_valid():
            order = form.save()
            print(f"Order created with ID (after save): {order.id}")
            return redirect(to='order_detail', order_id=order.id)
        else:
            print("Form is not valid")
            print(form.errors)
    else:
        form = OrderModelForm()

    return render(request, template_name="cestovani/order_new.html", context={"form": form})


def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, template_name="cestovani/order_detail.html", context={"order": order})


def order_list(request):
    orders = Order.objects.all()
    orders = list(orders)
    form = OrderModelForm(initial={"orders": orders})
    return render(request, template_name="cestovani/order_list.html", context={"form": form, "orders": orders})


def ticket_list(request):
    tickets = Ticket.objects.all()
    tickets = list(tickets)
    form = TicketModelForm(initial={"tickets": tickets})
    return render(request, template_name="cestovani/ticket_list.html", context={"form": form, "tickets": tickets})
