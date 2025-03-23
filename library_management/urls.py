from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Django admin site
    path('', include('library_app.urls')),  # All app URLs (both API and direct views)
]
