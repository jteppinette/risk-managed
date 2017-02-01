from django.conf.urls import include, url, static
from django.conf import settings

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from main import urls

urlpatterns = [
    url('^', include(urls)),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
