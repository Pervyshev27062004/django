from django.contrib import admin

from products.models import Product
from products.models import Purchase
from products.models import Address


class PurchaseAdminInline(admin.TabularInline):
    model = Purchase


class AddressAdminInline(admin.TabularInline):
    model = Address


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "description", "color", "created_at")
    fields = ("title", "image", "price", "description", "created_at")
    readonly_fields = ("created_at",)
    search_fields = ("title", "description")
    inlines = [PurchaseAdminInline]


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ("user", "product", "count", "created_at")
    fields = ("user", "product", "count", "created_at")
    readonly_fields = ("created_at",)
    search_fields = ("user__email", "products__title")


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("user", "country", "city", "address", "created_at")
    fields = ("user", "country", "city", "address", "created_at")
    readonly_fields = ("created_at",)
