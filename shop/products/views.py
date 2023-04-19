import logging

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.cache import cache

from products.models import Product, Purchase
from products.forms import ProductsForm

from django.contrib.auth.models import User

logger = logging.getLogger(__name__)


def index5(request):
    title = request.GET.get("title")
    purchases__count = request.GET.get("purchases__count")

    result = cache.get(f"products-view-{title}-{purchases__count}-{request.user.id}")
    if result is not None:
        return result

    products = Product.objects.all()

    if title is not None:
        products = products.filter(title__icontains=title)

    if purchases__count is not None:
        products = products.filter(purchases__count=purchases__count)

    response = render(request, "index.html", {"products": products})
    cache.set(f"products-view-{title}-{purchases__count}", response, 60 * 60)
    return response


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


def product(request):
    if request.method == "POST":
        form = ProductsForm(request.POST)
        if form.is_valid():
            Product.objects.create(
                title=form.cleaned_data['title'],
                price=form.cleaned_data['price'],
                color=form.cleaned_data['color'],
                excerpt=form.cleaned_data['excerpt'],
                description=form.cleaned_data['description'],
            )
            # Process validated data
            # form.cleaned_data["email"]
            logger.info(f"Create product: {form.cleaned_data['title']}")
            # form.cleaned_data["password"]
            logger.info(f"Product price: {form.cleaned_data['price']}")

            return redirect("/")
    else:
        form = ProductsForm()

    return render(request, "product.html", {"form": form})


def index4(request):
    products = Product.objects.all()

    title = request.GET.get("title")
    if title is not None:
        products = products.filter(title__icontains=title)

    purchases__count = request.GET.get("purchases__count")
    if purchases__count is not None:
        products = products.filter(purchases__count=purchases__count)

    return render(request, "index.html", {"products": products})
