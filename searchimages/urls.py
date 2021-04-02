from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.home, name="home"),
    path('SearchImages/', views.SearchImages.as_view(), name="Images"),
    path('FavouriteImages/', views.FavouriteImages.as_view(), name="FavouriteImages"),
    path('GeoLocationList/', views.GeoLocationList.as_view(), name="GeoLocationList"),
]+static(settings.MEDIA_URL,document_root=settings)