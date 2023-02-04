# apps/sekdilu139/urls.py

# Import from django modules
from django.urls import path

# Import from locals
from apps.sekdilu139 import views

app_name='sekdilu139'

urlpatterns = [
    path('', views.home_page, name='home_page'),
]
