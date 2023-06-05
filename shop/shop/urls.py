from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from products.views import index
from products.views import index1
from products.views import index2
from products.views import index3
from products.views import index4
from products.views import index5


from profiles.views import register, login_view, logout_view
from products.views import product


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls", namespace="api")),
    path("api/auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("", index5, name="index5"),
    path("register/", register, name="register"),
    path("product/", index4, name="product"),
    path("login_view/", login_view, name="login_view"),
    path("logout_view/", logout_view, name="logout_view"),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
