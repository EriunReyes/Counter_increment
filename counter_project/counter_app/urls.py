from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('destroy_session', views.destroy),
    path('addtwo', views.two),
    path('add_count', views.add_input)
]