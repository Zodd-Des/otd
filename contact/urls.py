from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    # path to admin page
    path('admin/', admin.site.urls),
    # path to acces the home page
    path('',views.index, name='index'),
    # path to send the form to the backend
    path('contact', views.contact, name='contact')
]