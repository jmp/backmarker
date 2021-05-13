from django.contrib import admin
from django.urls import include, path

from circuits import urls as circuits_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include((circuits_urls, "circuits"), namespace="circuits")),
]
