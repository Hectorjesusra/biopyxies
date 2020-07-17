from django.urls import path
from labapps import views

urlpatterns = [
    path('molemule', views.molemule, name='molemule'),
    path('acidos-nucleicos', views.acidos_nucleicos, name='acidos-nucleicos'),
    path('pyteins', views.pyteins, name='pyteins'),
]
