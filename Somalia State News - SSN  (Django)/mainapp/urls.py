from django.contrib import admin
from django.urls import path,include
from mainapp import views

urlpatterns = [
    path('', views.dp, name='home'),
    path('articles/', views.articles, name='articles'),
    path('job/', views.job, name='job'),
    path('breaking/', views.breaking, name='breaking'),
    path('editorial/', views.editorial, name='editorial'),
    path('details/<id>/', views.details, name='details'),
    path('about_us/', views.about_us, name='about_us'),
    path('contact_us/', views.contact_us, name='contact_us'),
]
