from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('portfolio', views.portfolio, name = 'portfolio'), 
    path('services', views.services, name = 'services'), 
    path('contact', views.contact, name = 'contact'),
    path('registration', views.registration, name = 'registration'),
    path('login', views.user_login, name = 'login'),
    # re_path('^renouvellement/<str:slug>', views.renouvellement, name="renouvellement"),
    
]