import views as views

from .import views
from django.urls import path,include

urlpatterns = [

    # path('',views.myweb,name='myweb'),
    # path('about/',views.about,name='about'),
    # path('contact/', views.about, name='contact'),
    # path('details/', views.details, name='details'),
    # path('thanku/', views.thanku, name='tanku'),

    path('', views.index, name='index'),
    path('calculate/', views.calculate, name='calculate'),
]


