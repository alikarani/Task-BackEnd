from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.home, name="home"),
    path('Images/', views.Images.as_view(), name="Images"),
]+static(settings.MEDIA_URL,document_root=settings)