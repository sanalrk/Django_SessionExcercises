from django.urls import path
from . import views
urlpatterns = [
    path('', views.set_name, name="set_name"),
    path('preference/', views.set_preference, name="preference"),
    path('display/', views.display, name="display"),
    path('clear_session/', views.clear_session, name="clear_session"),
]
