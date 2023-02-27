import logging
from django.http import HttpResponse
from django.conf import settings
logger = logging.getLogger(__name__)


def index(request):
    if request.GET.get("param"):
        logger.info(f"My custom var = {settings.MY_CUSTOM_VARIABLE}")
        logger.info(f"My env variable = {settings.MY_ENV_VARIABLE}")
        logger.info(f"My param = {request.GET.get('param')}")
        logger.info(f"My new var 1 = {settings.FOR_HOMEWORK1}")
        logger.info(f"My new var 2 = {settings.FOR_HOMEWORK2}")
        logger.info(f"My new var 3 = {settings.FOR_HOMEWORK3}")
    return HttpResponse("THIS IS PAGE NOT AVAILABLE! PLEASE WILL LEAVE IT!")
