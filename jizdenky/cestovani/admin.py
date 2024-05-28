from django.contrib import admin

# Register your models here.
from .models import Ticket, Order


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_filter = ["destination"]
    search_fields = ("destination",)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_filter = ["last_name"]
    search_fields = ("last_name",)
