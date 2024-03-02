from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('product/', listproduct, name='list'),
    path('category/', category, name='category'),
    path('product/<int:id>', productdetails, name='details'),
    path('add', productadd, name='add'),
    path('delete/<int:id>', deleteproduct, name='delete'),
    path('update/<int:id>', updateproduct, name='update'),
    # path('about/', about, name='about'),
    path('addform', productaddforms, name='addform'),
    path('productgenric/', Productlist.as_view(), name='productlist'),
    path('productgenric/<int:pk>', Productdetail.as_view(), name='productdetail'),
    path('updategenric/<int:pk>', Productupdate.as_view(), name='productupdate'),
    path('addgenric', Productadd.as_view(), name='addgenric'),
    path('deletegenric/<int:pk>', Deleteproduct.as_view(), name='deletegenric'),
    path('register/',register_user,name = 'register')

]