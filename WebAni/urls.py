from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import AnimeListView, SearchView

urlpatterns = [
    path('', AnimeListView.as_view(), name='home'),
    path('search/', SearchView.as_view(), name='search')
]

urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)