from . import views
from django.urls import path

urlpatterns = [
    path('homepage/', views.homepage),
    path('aboutus/', views.aboutus),
    path('contact/', views.contactus),
    path('login/', views.login),

]
