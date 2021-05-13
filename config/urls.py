from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from circuits import urls as circuits_urls

urlpatterns = [
    path("api/", include((circuits_urls, "circuits"), namespace="circuits")),
]

if settings.DEBUG:
    urlpatterns += [path("admin/", admin.site.urls)]
