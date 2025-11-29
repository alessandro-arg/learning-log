from django.contrib import admin
from .models import Customer, Order, Product, Producttype, Bill
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_filter = ['first_name', 'last_name']
    list_display = ['first_name', 'last_name', 'email_address', 'account']
    search_fields = ['first_name', 'last_name']



admin.site.register(Customer, CustomerAdmin)
admin.site.register(Bill)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Producttype)
