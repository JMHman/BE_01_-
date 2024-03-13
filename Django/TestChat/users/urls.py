from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
  TokenObtainPairView,
  TokenRefreshView,
  TokenVerifyView
)

urlpatterns = [
  path('', views.Users.as_view()), # api/v1/users/
  path('myinfo', views.MyInfo.as_view()), # api/v1/users/myinfo
  
  # Authentication
  path('gettoken', obtain_auth_token), # DRF token
  # Django Session
  path('login', views.Login.as_view()), # api/v1/users/login 
  path('logout', views.Logout.as_view()), # api/v1/users/logout
  
  # JWT Authentication
  path('login/jwt', views.JWTLogin.as_view()), # api/v1/users/logout/jwt
  path('login/jwt/info', views.UserDtailView.as_view()), # api/v1/users/login/jwt/info

  # Simple JWT Authentication (url은 대소문자 구별이 없다, 아니였다 url에서 대소문자를 구분해서 인식한다.))
  path('login/simpleJWT', TokenObtainPairView.as_view()), # api/v1/users/login/simpleJWT
  path('login/simpleJWT/refresh', TokenRefreshView.as_view()), # api/v1/users/login/simpleJWT/refresh
  path('login/simpleJWT/verify', TokenVerifyView.as_view()), # api/v1/users/login/simpleJWT/verify
]

{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwOTU0NTMwNSwiaWF0IjoxNzA4MzM1NzA1LCJqdGkiOiIzMDdkYTAxMzc5MjU0YjQ0ODc3NDI1MzA3ODBiMWI2MCIsInVzZXJfaWQiOjF9.SiqKibX3rfH51qNBYzEOJfYKliamF7TG7u51-VFE85Y",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA4MzM5MzA1LCJpYXQiOjE3MDgzMzU3MDUsImp0aSI6IjUxZmYzOWM5MDEyODRiOTlhZDQ5M2MwNmMyYTdlYTc1IiwidXNlcl9pZCI6MX0.NyaOufdAf5EK-Aqqnc7GJ7Lj3UhLwvJEh0HGo9j2hK8"
}
