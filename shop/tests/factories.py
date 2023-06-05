import factory

from decimal import Decimal

from products.models import Product

from factory.django import DjangoModelFactory


class ProductFactory(DjangoModelFactory):
    class Meta:
        model = Product

    title = factory.Faker("word")
    color = "RED"
    price = Decimal(100)
    price_eur = Decimal(290)
