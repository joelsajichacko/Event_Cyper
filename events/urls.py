"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from events import views
from users import views as signup_views

urlpatterns = [
    path('', views.home, name='home'),
    path('events/', views.events, name='events'),
    path('contact/', views.contact, name='contact'),
    path('signup/', signup_views.signup, name='signup'),
    path('eventpost/<str:slug>', views.eventpost, name='eventpost'),
    path('login/', views.login, name='login'),
    path('create_event/', views.create_event, name='create_event'),
]
