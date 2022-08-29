from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.loginuser, name='login'),
    path('featuredmatches/', views.featuredmatches, name='featuredmatches'),
    path('yourslots/', views.yourslots, name='yourslots'),
    path('bookaslot/', views.bookaslot, name='bookedaslot'),
    path('bookedslots/', views.bookedslots, name='bookedslots'),
    path('logout/', views.logoutuser, name='logout'),
    path('basketball/', views.basketball, name='basketball'),
    path('badminton/', views.badminton, name='badminton'),
    path('squash/', views.squash, name='squash'),
    path('volleyball/', views.volleyball, name='volleyball')
]