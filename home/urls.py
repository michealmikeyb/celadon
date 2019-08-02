from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    url(r'^display-page/(?P<page>[0-9a-zA-Z\-_]+)/$', views.display_pages, name='display-page'),
]