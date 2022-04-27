from django.urls import path
from . import views



urlpatterns = [
    path('home/', views.Home, name='skaterbase-home'),
    path('AboutSkater/', views.AboutSkater, name='skaterbase-AboutSkater'),
    path('signup/', views.signup, name='signup')
    
]