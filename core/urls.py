from core import views
from django.urls import path, include

app_name = 'core'

urlpatterns = [
    path('home/', views.hello, name='hello'),
]
