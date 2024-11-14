from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page, name='home_page'),
    path('rating/', views.submit_rating, name='rating'), 
    path('thanks/', views.thanks_page, name='thanks'),
]