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
    path('home1/<int:pk>/', views.home1, name='home1'),
    path('about/', views.about, name='about'),
    path('about1/<int:pk>/', views.about1, name='about1'),
    path('service/', views.service, name='service'),
    path('service1/<int:pk>/', views.service1, name='service1'),
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('logindata/', views.logindata, name='logindata'),
    path('register/', views.register, name='register'),
    path('alldata/', views.alldata, name='alldata'),
    path('dash/', views.dash, name='dash'),
    path('alldata1/<int:pk>/', views.alldata1, name='alldata1'),
    path('dashboard/<int:pk>/', views.dashboard, name='dashboard'),
    path('first/<int:pk>/', views.first, name='first'),
    path('last/<int:pk>/', views.last, name='last'),
    path('asc/<int:pk>/', views.asc, name='asc'),
    path('desc/<int:pk>/', views.desc, name='desc'),
    path('alld/<int:pk>/', views.alld, name='alld'),
    path('edit/<int:pk1>/<int:pk2>/', views.edit, name='edit'),
    path('edit_data/<int:pk1>/<int:pk2>/', views.edit_data, name='edit_data'),
 

    




    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
