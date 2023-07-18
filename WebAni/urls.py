from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import index, search

urlpatterns = [
    path('', index),
    path('search/', search, name='search')
]

urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)