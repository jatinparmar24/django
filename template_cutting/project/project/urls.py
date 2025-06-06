"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('about/' ,views.about,name='about'),
    path('about1/<int:pk>/',views.about1,name='about1'),
    path('terms/' ,views.terms,name='terms'),
    path('terms1/<int:pk>/',views.terms1,name='terms1'),
    path('services/' ,views.services,name='services'),
    path('service1/<int:pk>/', views.service1, name='service1'),
    path('login/' ,views.login,name='login'),
    path('registration/' ,views.registration,name='registration'),
    path('register/',views.register,name='register'),
    path('logindata/',views.logindata,name='logindata'),
    path('index/' ,views.index,name='index'),
    path('index1/<int:pk>/',views.index1,name='index1'),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
