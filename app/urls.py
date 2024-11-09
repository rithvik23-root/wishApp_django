from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('registration/', views.registration, name='registration'),
    path('users/', views.users, name='users'),
    path('gifts/', views.gifts, name='gifts'),
    path('other_users_gifts/<int:user_id>/', views.other_users_gifts, name='other_users_gifts'),
    path('error/', views.error, name='error'),
]
