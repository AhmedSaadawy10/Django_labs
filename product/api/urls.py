from django.urls import path
from .views import *

urlpatterns = [
    path("all/", getall),
    path('product/<int:pk>',getbyid),
    path('add/',add),
    path('del/<int:pk>',delete),
    path('update/<int:pk>',update)
]
