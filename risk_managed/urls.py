from django.contrib.staticfiles.urls import urlpatterns
from django.urls import include, path

urlpatterns += [path("", include("risk_managed.main.urls"))]
