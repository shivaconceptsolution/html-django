from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('about-us',views.about,name='about'),
    path('services',views.services,name='services'),
    path('contacts',views.contacts,name='contacts'),
    path('gallery',views.gallery,name='gallery'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('profile',views.profile,name='profile'),
    path('editprofile',views.editprofile,name='editprofile'),
    path('deleteprofile',views.deleteprofile,name='deleteprofile')

]