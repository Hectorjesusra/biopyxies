from django.urls import path, include
from lab import views

urlpatterns = [
    path('about', views.about, name='about'),
    path('apps', views.apps, name='apps'),
    path('apps/', include('labapps.urls'), name='apps'),
    path('tutorial', views.tutorial, name='tutorial'),
]
