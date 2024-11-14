# primetime/backend/urls.py
from django.urls import path
from . import views  # Import the views of the backend app

urlpatterns = [
    path('check_prime/', views.check_prime, name='check_prime'),  # Define the prime-check view
]
