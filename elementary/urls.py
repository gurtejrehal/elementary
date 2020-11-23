"""elementary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from core.models import Customize, QuizTakers


elementary = Customize.objects.all()[0]
ranks = QuizTakers.objects.filter(user__user__is_staff=False).order_by("-correct_answers")
top_ranks = ranks[:3]
rest_ranks = ranks[3:]

extra_context = {
    'elementary': elementary,
    'top_ranks': top_ranks,
    'rest_ranks': rest_ranks
}

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('oauth/', include('social_django.urls', namespace='social')),
                  path('',
                       auth_views.LoginView.as_view(extra_context=extra_context), name='auth_login'),
                  path('accounts/', include('registration.backends.simple.urls')),
                  path('', include('core.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
