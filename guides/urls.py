from django.urls import path
from . import views

app_name = 'guides'

urlpatterns = [
    path('', views.get_home, name='home')
]