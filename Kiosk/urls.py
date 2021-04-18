from django.urls import path
from . import views
from .views import homepage, customerlist, customerform, foodlist, vieworders, deleteorder,editordersform,addordersform

urlpatterns=[
    path('grabgrub', views.homepage, name='homepage'),
    path('grabgrub/viewcustomers.html/',views.customerlist,name='customerlist'),
    path('grabgrub/customer.html/',views.customerform,name='customerform'),
    path('<int:id>/customer', views.customerform,name="customerupdate"),
    path('<int:pk>/customerorder', views.customerorder,name="customerorder"),
    path('grabgrub/viewfood.html/', views.foodlist,name="foodlist"),
    path('grabgrub/food.html/',views.foodform,name='foodform'),
    path('<int:id>/food', views.foodform,name="foodupdate"),
    path('grabgrub/vieworders.html/',views.vieworders,name='vieworders'),
    path('grabgrub/order.html/',views.addordersform,name='orderform'),
    path('order/<int:pk>', views.editordersform,name="editordersform"),
    path('delete/<int:pk>', views.deleteorder,name='deleteorder'),
]