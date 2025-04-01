from django.contrib import admin
from django.urls import path
from home import views  # Import your view here


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Set the home view as the root URL
]
