from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from django.urls import path
from . import views

def home(request):
    return JsonResponse({"status": "Django backend is running!"})

urlpatterns = [
    path('api/', views.api_home),                  # <-- ADD THIS
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]

