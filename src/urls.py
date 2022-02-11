from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .views import Index

app_name = 'src'

urlpatterns = [

    path('', Index.as_view() ,name="index"),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
