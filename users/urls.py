"""URL schema for users."""

from django.urls import path, include
from . import views

app_name = 'users'
urlpatterns = [
    # Login page
    path('', include('django.contrib.auth.urls')),
    path('logout/', views.logged_out, name='logged_out'),
    path('register/', views.register, name='register'),
]
