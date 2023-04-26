import logging
from products.models import Product
import requests
from django.core.management.base import BaseCommand
from django_rq import job
from decimal import Decimal
from django.db.models import F


logger = logging.getLogger(__name__)


@job
def update_products():
    response = requests.get("https://www.nbrb.by/api/exrates/rates?periodicity=0")
    result = response.json()
    item = None
    for item in result:
        if item["Cur_Abbreviation"] == "EUR":
            break

    if item is not None:
        for product in Product.objects.all():
            product.price_eur = product.price / Decimal(item["Cur_OfficialRate"])
            product.save()

        Product.objects.all().update(
            price_eur=F("price") / Decimal(item["Cur_OfficialRate"])
        )


class Command(BaseCommand):
    help = "Update products"

    def handle(self, *args, **options):
        update_products()
