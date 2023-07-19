from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.logout, name='signout'),
    path('cart/', views.CART, name='cart'),
]
