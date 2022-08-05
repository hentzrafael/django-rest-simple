from django.urls import path
from . import views

urlpatterns = [
    path('',views.getData),
    path('add/',views.addItem),
    path('last/',views.getLastInserted),
    path('addUser/',views.addUser),
    path('users/',views.getUsers)
]