from django.urls import path, re_path
from django.views.generic import RedirectView
import re

from . import views

urlpatterns = [
    re_path(r'^$', RedirectView.as_view(url='foodbank/')),
    path('about/', views.about, name='about'),
    path('foodbank/', views.index, name='index'),
]