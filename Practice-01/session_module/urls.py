from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('initialise/', views.initialise, name="initialise"),
    path('increment/', views.increment, name="increment"),
    path('show/', views.show, name="show"),
]
