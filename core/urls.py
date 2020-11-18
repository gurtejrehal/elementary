from core import views
from django.urls import path

app_name = 'core'

urlpatterns = [
    path('play/', views.index, name='index'),
    path('answer/', views.answer, name='answer'),
    path('search/', views.search, name='search'),
    path('notifications/', views.notifications, name='notifications'),
    path('toggle-mode/', views.toggle_mode, name="toggle"),
    path('color-mode/', views.color_mode_toggle, name="color_mode"),
    path('profile/<username>/', views.profile, name='profile'),
    path('settings/', views.settings, name='settings'),
]
