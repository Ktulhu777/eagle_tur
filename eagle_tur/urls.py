from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('guides.urls', namespace='guides')),
    path('user/', include('users.urls', namespace='users')),
]
