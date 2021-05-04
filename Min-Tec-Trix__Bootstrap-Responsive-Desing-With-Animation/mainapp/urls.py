from django.contrib import admin
from django.urls import path,include
from mainapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about_us/', views.about_us, name='about_us'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('service/', views.service, name='service'),
    path('contact_us/send_mail/', views.send_mail, name='send_mail'),
]
