import logging

from django.conf import settings
from django.http import HttpResponse

logger = logging.getLogger(__name__)
from products.models import Product, Purchase


def index(request):
    if request.GET.get("param"):
        logger.info(f"My custom var = {settings.MY_CUSTOM_VARIABLE}")
        logger.info(f"My env variable = {settings.MY_ENV_VARIABLE}")
        logger.info(f"My param = {request.GET.get('param')}")
        logger.info(f"My new var 1 = {settings.FOR_HOMEWORK1}")
        logger.info(f"My new var 2 = {settings.FOR_HOMEWORK2}")
        logger.info(f"My new var 3 = {settings.FOR_HOMEWORK3}")
    return HttpResponse("THIS IS PAGE NOT AVAILABLE! PLEASE WILL LEAVE IT!")


def index1(request):
    products = Product.objects.all()
    query = request.GET.get("query")
    if query is not None:
        products = products.filter(title__icontains=query)
    string = "<br>".join([str(p) for p in products])
    return HttpResponse(string)


def index2(request):
    products = Product.objects.filter(purchases__user__email="kingtiger27062004@gmail.com")
    string = "<br>".join([str(p) for p in products])
    return HttpResponse(string)


def index3(request):
    products = Product.objects.all()

    title = request.GET.get("title")
    if title is not None:
        products = products.filter(title__icontains=title)

    purchases__count = request.GET.get("purchases__count")
    if purchases__count is not None:
        products = products.filter(purchases__count=purchases__count)

    string = "<br>".join([str(p) for p in products])
    return HttpResponse(string)


