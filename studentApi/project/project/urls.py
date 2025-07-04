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
from django.urls import path, include
from app.views import *
from rest_framework import routers
# method for token
# from rest_framework.authtoken import views
from rest_framework_simplejwt.views  import TokenObtainPairView,TokenRefreshView




router = routers.DefaultRouter()
router.register(r'students', StudentViewSet),
router.register(r'teachers',TeacherViewSet),


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include(router.urls)),

    # method for token
    # path('api-token-auth/', views.obtain_auth_token),
    # method for token

    # method for customtoken
    # path('api-token-auth/', CustomAuthToken.as_view()),

    # method for token

    # "for simple jwt"
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # "for simple jwt"



    # for authentication and persmission login
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))


]
