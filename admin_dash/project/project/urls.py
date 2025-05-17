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
    path('', views.home,name='home'),
    path('admindata/', views.admindata,name='admindata'),
    path('home1/', views.home1,name='home1'),
    path('admindata1/', views.admindata1,name='admindata1'),
    path('userlogin/', views.userlogin,name='userlogin'),
    path('login/', views.login,name='login'),
    path('logout/', views.logout,name='logout'),
    path('admin_login/', views.admin_login,name='admin_login'),
    path('add_emp/', views.add_emp, name='add_emp'),
    path('show_all_emp/', views.show_all_emp, name='show_all_emp'),
    path('userdetail/', views.userdetail, name='userdetail'),
    path('user_ask/', views.user_ask, name='user_ask'),
    path('user_info/', views.user_info, name='user_info'),
    path('edit_emp/<int:id>/', views.edit_emp, name='edit_emp'),
    path('delete_employee/<int:id>/', views.delete_employee, name='delete_employee'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
