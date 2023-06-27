from django.contrib import admin
from django.urls import path

from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('',include('core.urls')),
    path('', views.home, name='home'),
    path('results', views.results, name='results'),
]
