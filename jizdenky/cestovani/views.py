from django.shortcuts import render, reverse, get_object_or_404
from .forms import OrderModelForm
from .forms import TicketModelForm
from .models import Ticket, Order
from django.http import HttpResponseRedirect
import uuid


def homepage(request):
    return render(request, template_name="cestovani/homepage.html")


# Create your views here.

def order_new(request):
    if request.method == "POST":
        form = OrderModelForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            order = Order(id=uuid.uuid4(), **data)
            print(order)
            order.save()
            return HttpResponseRedirect(reverse('jizdenky:order_detail', args=(order.id,)))
        else:
            print("Form is not valid")
            print(form.errors)
    else:
        form = OrderModelForm()

    return render(request, template_name="cestovani/order_new.html", context={"form": form})


def order_detail(request, id):
    order = get_object_or_404(Order, id=id)
    return render(request, template_name="cestovani/order_detail.html", context={"order": order})


def order_end(request):
    return render(request, template_name="cestovani/order_end.html")


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
