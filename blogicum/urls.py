from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),  # Убрали namespace отсюда
    path('pages/', include('pages.urls')),  # Убрали namespace отсюда
]
