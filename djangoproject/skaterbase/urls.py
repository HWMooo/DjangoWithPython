from django.urls import path
from . import views



urlpatterns = [
    path('home/', views.Home, name='skaterbase-home'),
    path('AboutSkater/', views.AboutSkater, name='skaterbase-AboutSkater'),
    path('signup/', views.signup, name='signup'),
    path('account_activation_sent/', views.account_activation_sent, name='account_activation_sent'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate')
    
]