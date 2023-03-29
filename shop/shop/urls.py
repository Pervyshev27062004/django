"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from products.views import index
from products.views import index1
from products.views import index2
from products.views import index3
from products.views import index4

from profiles.views import register, login_view, logout_view
from products.views import product


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("api.urls", namespace="api")),
    path("api/auth/", include("rest_framework.urls", namespace="rest_framework")),
    path('', index3, name="index"),
    path('register/', register, name="register"),
    path('product/', index4, name="product"),
    path('login_view/', login_view, name="login_view"),
    path('logout_view/', logout_view, name="logout_view")

]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
