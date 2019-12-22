from django.urls import path
from . import views #import views


# adding url
urlpatterns = [
    path('', views.index, name='home'), #home
    path('portfolio', views.portfolio, name='portfolio'), #portfolio
    path('contact', views.contact, name='contact'), #contact
     path('login', views.login, name='login'), #login
      path('register', views.register, name='register'), #register
]