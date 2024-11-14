from django.contrib import admin
from django.urls import path, include  # `include` allows you to include app-level urls

urlpatterns = [
    path('admin/', admin.site.urls),  # URL pattern for the Django admin page
    path('api/', include('prime_checker.urls')),  # Include URLs from the 'backend' app
]
