from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .views import Login, Logout

app_name = 'usuarios'

urlpatterns = [

    path('login/', Login.as_view() ,name="login"),
    path('logout/', Logout.as_view() ,name="logout"),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
