from django.conf.urls import include, url

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from main import urls

urlpatterns = [
    url('^', include(urls)),
]

urlpatterns += staticfiles_urlpatterns()
