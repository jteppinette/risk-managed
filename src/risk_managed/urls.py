from django.conf.urls import include, url

from django.contrib.staticfiles.urls import urlpatterns

from risk_managed.main import urls

urlpatterns += [
    url('^', include(urls)),
]
